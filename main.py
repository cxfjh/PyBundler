import os
import subprocess
import sys
import warnings
from ctypes import windll
from threading import Thread
from PyQt6 import QtCore, QtGui, QtWidgets


# 忽略 DeprecationWarning 警告
warnings.filterwarnings("ignore", category=DeprecationWarning)


# 实例化UI界面
class PackingAssistantUI:
    def __init__(self):
        # 初始化文件路径、图标路径和目录路径
        self.filePath = ""
        self.iconPath = ""
        self.dirPath = ""

    def setupUi(self, form):
        # 设置窗口的基本属性
        form.setObjectName("Form")
        form.resize(370, 380)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        form.setFont(font)
        form.setWindowFlags(form.windowFlags() | 0x40000)
        
        # 设置窗口图标
        iconPath = os.path.join(os.path.dirname(__file__), 'src', 'static', 'icon.ico')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconPath), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        form.setWindowIcon(icon)
        form.setFixedSize(form.width(), form.height())

        # 创建垂直布局的容器
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 80, 271, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        # 设置垂直布局
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # 添加复选框：禁用控制台
        self.consoleDisableCheckbox = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.consoleDisableCheckbox.setObjectName("consoleDisableCheckbox")
        self.verticalLayout.addWidget(self.consoleDisableCheckbox)

        # 添加复选框：管理员权限
        self.adminPermissionCheckbox = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.adminPermissionCheckbox.setObjectName("adminPermissionCheckbox")
        self.verticalLayout.addWidget(self.adminPermissionCheckbox)

        # 添加复选框：单个文件
        self.singleFileCheckbox = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.singleFileCheckbox.setObjectName("singleFileCheckbox")
        self.verticalLayout.addWidget(self.singleFileCheckbox)

        # 添加图标选择布局
        self.iconLayout = QtWidgets.QHBoxLayout()
        self.iconLayout.setObjectName("iconLayout")

        # 添加选择图标按钮
        self.selectIconButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.selectIconButton.setObjectName("selectIconButton")
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.selectIconButton.setFont(font)
        self.iconLayout.addWidget(self.selectIconButton)

        # 添加图标路径输入框
        self.iconPathInput = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(8)
        self.iconPathInput.setFont(font)
        self.iconPathInput.setObjectName("iconPathInput")
        self.iconLayout.addWidget(self.iconPathInput)
        self.verticalLayout.addLayout(self.iconLayout)

        # 添加目录选择布局
        self.dirLayout = QtWidgets.QHBoxLayout()
        self.dirLayout.setObjectName("dirLayout")

        # 添加选择目录按钮
        self.selectDirButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.selectDirButton.setObjectName("selectDirButton")
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.selectDirButton.setFont(font)
        self.dirLayout.addWidget(self.selectDirButton)

        # 添加目录路径输入框
        self.dirPathInput = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(8)
        self.dirPathInput.setFont(font)
        self.dirPathInput.setObjectName("dirPathInput")
        self.dirLayout.addWidget(self.dirPathInput)
        self.verticalLayout.addLayout(self.dirLayout)

        # 添加选择文件按钮
        self.selectFileButton = QtWidgets.QPushButton(parent=form)
        self.selectFileButton.setGeometry(QtCore.QRect(40, 30, 90, 30))
        self.selectFileButton.setObjectName("selectFileButton")

        # 添加打包按钮
        self.packButton = QtWidgets.QPushButton(parent=form)
        self.packButton.setGeometry(QtCore.QRect(220, 310, 100, 35))
        self.packButton.setObjectName("packButton")

        # 添加文件路径输入框
        self.filePathInput = QtWidgets.QLineEdit(parent=form)
        self.filePathInput.setGeometry(QtCore.QRect(140, 30, 190, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.filePathInput.setFont(font)
        self.filePathInput.setObjectName("filePathInput")

        # 添加版本标签
        self.versionLabel = QtWidgets.QLabel(parent=form)
        self.versionLabel.setGeometry(QtCore.QRect(320, 360, 41, 16))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(8)
        self.versionLabel.setFont(font)
        self.versionLabel.setObjectName("versionLabel")

        # 添加关于按钮
        self.aboutButton = QtWidgets.QPushButton(parent=form)
        self.aboutButton.setGeometry(QtCore.QRect(50, 310, 100, 35))
        self.aboutButton.setObjectName("aboutButton")

        # 翻译UI
        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        # 设置UI元素的文本内容
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "PyBundler"))
        self.consoleDisableCheckbox.setText(_translate("Form", "禁用控制台"))
        self.adminPermissionCheckbox.setText(_translate("Form", "管理员权限"))
        self.singleFileCheckbox.setText(_translate("Form", "单个文件"))
        self.selectIconButton.setText(_translate("Form", "选择图标"))
        self.selectDirButton.setText(_translate("Form", "选择目录"))
        self.selectFileButton.setText(_translate("Form", "选择文件"))
        self.packButton.setText(_translate("Form", "打包"))
        self.versionLabel.setText(_translate("Form", "v1.0.0"))
        self.aboutButton.setText(_translate("Form", "关于"))

        # 绑定按钮点击事件
        ui.selectFileButton.clicked.connect(selectFile)
        ui.selectIconButton.clicked.connect(selectIcon)
        ui.selectDirButton.clicked.connect(selectDir)
        ui.aboutButton.clicked.connect(about)
        ui.packButton.clicked.connect(lambda: Thread(target=getCheckboxSelections).start())


# 支持拖拽的窗口类
class DragDropWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            filePath = url.toLocalFile()
            if os.path.isfile(filePath):
                if filePath.endswith('.py'):
                    ui.filePathInput.setText(filePath)
                    ui.filePath = os.path.dirname(filePath)
                elif filePath.lower().endswith(('.ico', '.png', '.jpg')):
                    ui.iconPathInput.setText(filePath)
                    ui.iconPath = filePath
            elif os.path.isdir(filePath):
                ui.dirPathInput.setText(filePath)
                ui.dirPath = filePath
        event.acceptProposedAction()


# 选择文件
def selectFile():
    try:
        filePath = QtWidgets.QFileDialog.getOpenFileName(None, "选择文件", os.getcwd(), "All Files (*.py)")[0]
        if filePath:
            ui.filePathInput.setText(filePath)
            ui.filePath = os.path.dirname(filePath)
    except: pass


# 选择图标
def selectIcon():
    try:
        iconPath = QtWidgets.QFileDialog.getOpenFileName(None, "选择图标", os.getcwd(), "Images (*.ico *.png *.jpg)")[0]
        if iconPath:
            ui.iconPath = iconPath
            ui.iconPathInput.setText(iconPath)
    except: pass


# 选择目录
def selectDir():
    try:
        dirPath = QtWidgets.QFileDialog.getExistingDirectory(None, "选择目录", os.getcwd())
        if dirPath:
            ui.dirPath = dirPath
            ui.dirPathInput.setText(dirPath)
    except: pass


# 关于
def about():
    text = """
    作者: fjh

    版本: v1.0.0

    联系: 2449579731@qq.com

    说明: 打包 Python 脚本的工具, 有问题请联系作者。

    注意: 请确保已拥有 Python 环境。
    """
    
    msgBox = QtWidgets.QMessageBox()
    msgBox.setWindowTitle("关于")
    msgBox.setText(text)
    msgBox.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'src', 'static', 'icon.ico')))
    msgBox.setWindowFlags(msgBox.windowFlags() | QtCore.Qt.WindowType.WindowStaysOnTopHint)
    msgBox.exec()


# 检查依赖
def checkDependencies():
    try: import PyInstaller
    except: subprocess.run("pip install pyinstaller -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple", shell=True, creationflags=subprocess.CREATE_NO_WINDOW)


# 获取选择并打包
def getCheckboxSelections():
    # 获取用户选择的参数
    adminPermission = "--uac-admin " if ui.adminPermissionCheckbox.isChecked() else ""
    disableConsole = "-w " if ui.consoleDisableCheckbox.isChecked() else ""
    singleFile = "-F " if ui.singleFileCheckbox.isChecked() else ""
    iconPath = f"-i {ui.iconPath} " if ui.iconPath else ""
    addData = f'--add-data "{ui.dirPath};{os.path.basename(ui.dirPath)}" ' if ui.dirPath else ""

    # 处理路径
    fileName = os.path.splitext(os.path.basename(ui.filePathInput.text()))[0]
    distPath = f'--distpath "./{fileName}" '
    workPath = f'--workpath "./{fileName}TempBuild" '

    # 构建 PyInstaller 命令
    command = f"pyinstaller --noconfirm {distPath}{workPath}{adminPermission}{disableConsole}{singleFile}{iconPath}{addData}{ui.filePathInput.text()}"
    if ui.filePathInput.text() == "": windll.user32.MessageBoxW(None, "请选择文件！", "错误", 0x0 | 0x10 | 0x40000); return

    # 禁用打包按钮，防止重复点击
    ui.packButton.setEnabled(False)
    ui.packButton.setText("正在打包")

    # 运行命令
    try:
        checkDependencies()
        os.chdir(ui.filePath)

        # 运行 PyInstaller
        subprocess.run(command, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        
        # 清理临时文件
        subprocess.run("powershell Remove-Item *.spec", shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        subprocess.run(f"powershell Remove-Item -Recurse -Force {fileName}TempBuild", shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        
        # 提示打包成功
        windll.user32.MessageBoxW(None, "打包成功！", "提示", 0x0 | 0x40 | 0x40000)
        os.startfile(os.path.join(os.getcwd(), fileName))
    except: windll.user32.MessageBoxW(None, "打包失败!", "错误", 0x0 | 0x10 | 0x40000)
    finally:
        ui.packButton.setEnabled(True)
        ui.packButton.setText("打包")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = DragDropWidget()
    ui = PackingAssistantUI()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec())


