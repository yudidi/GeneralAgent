参考: docs/develop.md

3.使用虚拟环境（最佳实践）：
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 安装包
pip install GeneralAgent
```

建议使用第3种方案（虚拟环境），因为：

- 避免权限问题
- 不会污染系统 Python 环境
- 项目依赖隔离，更容易管理
- 符合 Python 开发最佳实践
错误原因解释：

- [Errno 13] Permission denied : 表示当前用户没有写入权限
- 这通常发生在尝试向系统 Python 目录写入时
- 系统目录通常需要管理员权限