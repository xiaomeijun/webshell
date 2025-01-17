#!/bin/bash
#sean
#20250117
#功能mysql导出表 

#修改下面变量
# 设置数据库用户名、密码和数据库名
USER=""
PASSWORD=""
DATABASE=""
SQL_DIR=""  # 存放导出 SQL 文件的目录
HOST=""

# 表名列表
TABLES=(
  "表名1"
  "表名2"
  "表名3"
)




# 循环导出每个表的 SQL 文件
for TABLE in "${TABLES[@]}"; do
  SQL_FILE="${SQL_DIR}/${TABLE}.sql"
  echo "正在导出 $TABLE..."
  
  # 使用 mysqldump 导出表
  mysqldump -h $HOST -u $USER -p$PASSWORD $DATABASE $TABLE > "$SQL_FILE"
  
  # 检查是否成功导出
  if [ $? -eq 0 ]; then
    echo "$TABLE 导出完成!"
  else
    echo "$TABLE 导出失败!"
  fi
done

echo "所有表导出完成!"
