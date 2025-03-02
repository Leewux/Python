import sys
import os
from datetime import datetime
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Font, Border, Alignment, PatternFill
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from tkinter import Tk, filedialog  
import Ui_main 

def copy_cell_style(src_cell, dst_cell):
    """深度复制单元格样式"""
    # 复制字体
    dst_cell.font = Font(
        name=src_cell.font.name,
        size=src_cell.font.size,
        bold=src_cell.font.bold,
        italic=src_cell.font.italic,
        color=src_cell.font.color
    )
    
    # 复制边框
    dst_cell.border = Border(
        left=src_cell.border.left,
        right=src_cell.border.right,
        top=src_cell.border.top,
        bottom=src_cell.border.bottom
    )
    
    # 复制对齐方式
    dst_cell.alignment = Alignment(
        horizontal=src_cell.alignment.horizontal,
        vertical=src_cell.alignment.vertical,
        wrap_text=src_cell.alignment.wrap_text
    )
    
    # 复制填充样式
    # if src_cell.fill.start_color.index:
    #     dst_cell.fill = PatternFill(
    #         start_color=src_cell.fill.start_color,
    #         end_color=src_cell.fill.end_color,
    #         fill_type=src_cell.fill.fill_type
    #     )
    
    # 复制数字格式
    dst_cell.number_format = src_cell.number_format

class MainWindow(QMainWindow, Ui_main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 初始化文件列表
        self.selected_files = []

        # 连接按钮点击事件
        self.openButton.clicked.connect(self.open_files)
        self.Button_start.clicked.connect(self.process_files)  # 连接开始清算按钮

        # 修正你的输入提示
        self.lineEdit_name.setPlaceholderText("输入需要清算的人名")

    def open_files(self):
        # 隐藏tkinter主窗口
        Tk().withdraw()

        # 关键代码：多选文件对话框
        files = filedialog.askopenfilenames(
            title="选择文件",
            filetypes=[("Excel Files", "*.xlsx")]  # 文件过滤器
        )
        if files:
            # 将选中的文件路径显示在输入框（用逗号分隔）
            self.lineEdit_filename.setText(", ".join(files))
            self.selected_files = files  # 保存选中的文件路径

    def find_header(self, ws):
        """查找标题行"""
        for row in ws.iter_rows(max_row=20):
            current_values = [str(cell.value).strip() if cell.value else None for cell in row]
            if "金额(元)" in current_values and "承租人" in current_values:
                return row[0].row, {
                    "承租人": current_values.index("承租人") + 1,
                    "金额(元)": current_values.index("金额(元)") + 1
                }
        return None, None
    
    def process_files(self):
       
        if not self.selected_files:
            QMessageBox.warning(self, "警告", "请先选择文件!")
            return

        name = self.lineEdit_name.text().strip()  # 获取并去除空格
        if not name:
            QMessageBox.warning(self, "警告", "请输入需要清算的人名!")
            return

        # 创建一个总的工作簿
        total_wb = Workbook()
        total_ws = total_wb.active
        total_ws.title = "汇总结果"
        
        found_records = False  # 标记是否找到记录
        invalid_files = []  # 存储完全无效的文件

        for file in self.selected_files:

            file_has_valid_sheet = False  # 标记当前文件是否有有效工作表
            wb = load_workbook(file, read_only=False)

            # 第一次遍历：检查文件有效性
            has_any_valid = False
            for sheet_name in wb.sheetnames:
                ws = wb[sheet_name]
                if self.find_header(ws)[0]:  # 简单检查有效性
                    has_any_valid = True
                    break
            if not has_any_valid:
                invalid_files.append(os.path.basename(file))
                wb.close()
                continue
            
            print(f"处理文件: {file}") 
            # 遍历所有工作表
            for sheet_name in wb.sheetnames:
                ws = wb[sheet_name]
                header_row, col_mapping = self.find_header(ws)  # 传递当前工作表
                if not header_row:
                    continue
                file_has_valid_sheet = True

                match_count = 0  # 记录当前工作表匹配的数量
                # 复制表头（带完整样式）
                header_cells = ws[header_row]
                for idx, cell in enumerate(header_cells[2:], start=1):
                    new_cell = total_ws.cell(row=1, column=idx, value=cell.value)
                    copy_cell_style(cell, new_cell)
                # 数据迁移（带完整样式）
                for src_row in ws.iter_rows(min_row=header_row+1):
                    name_cell = src_row[col_mapping["承租人"]-1]
                    if not name_cell.value or str(name_cell.value).strip() != name:
                        continue
                    new_row_num = total_ws.max_row + 1
        
                    # 复制行高
                    total_ws.row_dimensions[new_row_num].height = ws.row_dimensions[src_row[0].row].height
                    match_count += 1
                    found_records = True  # 找到记录，更新标记
                    # 复制单元格数据和样式
                    for col_idx, src_cell in enumerate(src_row[2:], start=1):
                        new_cell = total_ws.cell(row=new_row_num, column=col_idx, value=src_cell.value)
                        copy_cell_style(src_cell, new_cell)
                    # 将记录添加到总的工作簿
                    #total_ws.append([sheet_name, name_cell.value, src_row[col_mapping["金额(元)"]-1].value])

                #print(f"在工作表 '{sheet_name}' 中找到 {match_count} 条记录")

            wb.close()
            if not file_has_valid_sheet:
                invalid_files.append(os.path.basename(file))
            # 最终错误处理
        if invalid_files:
            msg = "以下文件完全无效（所有工作表均无有效表头）：\n" + "\n".join(invalid_files)
            QMessageBox.warning(self, "文件错误", msg)
        # 如果找到了记录，则保存总的工作簿
        if found_records:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_name = f"{name}_汇总结果_{timestamp}.xlsx"
            total_wb.save(output_name)
            #print(f"生成文件：{output_name}")
            QMessageBox.information(self, "成功", f"生成文件：{output_name}")
            # 打开文件所在文件夹
            folder_path = os.path.dirname(os.path.abspath(output_name))
            os.startfile(folder_path)  # Windows
        else:
            QMessageBox.warning(self, "失败", f"未找到任何{name}的记录，未生成文件。")
            #print("未找到任何匹配的记录，未生成文件。")
        total_wb.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
