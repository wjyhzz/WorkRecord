# Linux 命令实操练习

### 一、基础路径与目录操作

1. 打开终端，先查看当前所在目录（验证`pwd`命令）：

    ```Bash
    pwd
    ```

2. 切换到当前用户的家目录（使用`~`表示绝对路径）：

    ```Bash
    cd ~
    ```

3. 在家目录下创建一个名为`linux_practice`的练习目录（验证`mkdir`命令）：

    ```Bash
    mkdir linux_practice
    ```

4. 切换到刚创建的目录（使用相对路径）：

    ```Bash
    cd linux_practice
    ```

5. 列出当前目录内容（此时应为空，验证`ls`命令）：

    ```Bash
    ls
    ```

### 二、文件创建与基本操作

1. 在`linux_practice`目录下创建3个测试文件（验证`touch`命令）：

    ```Bash
    touch file1.txt file2.txt note.md
    ```

2. 再次列出目录内容，确认文件创建成功：

    ```Bash
    ls
    ```

3. 向上切换到上一层目录（使用`..`表示相对路径），再查看当前目录：

    ```Bash
    cd ..
    pwd  # 此时应显示家目录路径
    ```

4. 再切换回`linux_practice`目录（使用绝对路径，需替换`用户名`为你的实际用户名）：

    ```Bash
    cd /home/用户名/linux_practice  # 例如：/home/wjy/linux_practice
    ```

### 三、mv命令练习（移动/重命名）

1. 将`file1.txt`重命名为`data.txt`（验证重命名功能）：

    ```Bash
    mv file1.txt data.txt
    ls  # 确认文件名已变更
    ```

2. 在当前目录下创建一个`docs`子目录，用于测试移动功能：

    ```Bash
    mkdir docs
    ```

3. 将`file2.txt`移动到`docs`目录中：

    ```Bash
    mv file2.txt docs/
    ls docs/  # 确认file2.txt已在docs目录内
    ```

4. 将`note.md`移动到`docs`目录并同时重命名为`readme.md`：

    ```Bash
    mv note.md docs/readme.md
    ls docs/  # 确认文件已移动且重命名
    ```

5. 测试“安全移动”（避免误覆盖）：先在`docs`目录创建一个`data.txt`，再尝试移动当前目录的`data.txt`到`docs`：

    ```Bash
    touch docs/data.txt  # 先在docs中创建同名文件
    mv -i data.txt docs/  # 使用-i选项，会提示是否覆盖，输入n不覆盖
    ```

### 四、cp命令练习（复制）

1. 复制`docs/readme.md`到当前目录，并重命名为`copy_readme.md`：

    ```Bash
    cp docs/readme.md copy_readme.md
    ls  # 确认复制成功
    ```

2. 递归复制`docs`目录到当前目录，并命名为`docs_backup`（验证`-r`选项）：

    ```Bash
    cp -r docs docs_backup
    ls  # 确认docs_backup目录存在
    ls docs_backup/  # 确认内部文件与docs一致
    ```

3. 测试“安全复制”（覆盖前提示）：复制`copy_readme.md`到`docs`目录，使用`-i`选项：

    ```Bash
    cp -i copy_readme.md docs/  # 会提示是否覆盖，输入y确认
    ```

4. 测试“显示复制过程”（使用`-v`选项）：

    ```Bash
    cp -v data.txt docs_backup/  # 会显示复制的文件路径
    ```

### 五、快捷键与异常处理

1. 故意执行一个会“卡住”的命令（如`sleep 100`，让程序休眠100秒）：

    ```Bash
    sleep 100
    ```

2. 立即按下`ctrl+c`停止命令执行（验证停止快捷键）。

### 六、清理练习环境（可选）

完成练习后，可删除测试目录（谨慎操作，确保目录内无重要文件）：

```Bash
cd ~  # 回到家目录
rm -r linux_practice  # 递归删除整个练习目录
```

通过以上步骤，可覆盖笔记中`pwd`/`ls`/`cd`/`touch`/`mkdir`/`mv`/`cp`的核心用法，以及`相对路径`/`绝对路径`、命令选项（`-i`/`-r`/`-v`）和`ctrl+c`快捷键的使用。重复2-3次可熟练掌握。
> （注：文档部分内容可能由 AI 生成）