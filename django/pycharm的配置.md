1. 确保已正确设置了您的项目结构。在 PyCharm 中，确保您的 Django 项目是作为一个单独的项目打开的，并且项目根目录（包含 `manage.py` 文件的目录）被设置为源代码根目录。
2. 配置项目解释器。在 "File" -> "Settings" -> "Project: <project_name>" -> "Project Interpreter" 中，选择您的 Python 解释器以及包含 Django 的依赖项的虚拟环境或系统级安装。
3. 启用 Django 支持。在 "File" -> "Settings" -> "Languages & Frameworks" -> "Django" 中，确保已启用 Django 支持并设置了正确的 Django 版本和项目路径。
4. 如果上述步骤均已完成但仍然出现错误，请尝试使用 "File" -> "Invalidate Caches / Restart" 重启 PyCharm 并清除缓存。