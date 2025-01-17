#!/bin/bash

# 设置数据库用户名、密码和数据库名
USER=""
PASSWORD=""
DATABASE=""
SQL_DIR=""  # 存放 SQL 文件的目录
HOST=""

# 表名列表
TABLES=(
  "表名"
  ""
  ""
)

# 循环导入每个表的 SQL 文件
for TABLE in "${TABLES[@]}"; do
  SQL_FILE="${SQL_DIR}/${TABLE}.sql"
  if [ -f "$SQL_FILE" ]; then
    echo "正在导入 $SQL_FILE..."
    mysql -h $HOST -u $USER -p$PASSWORD $DATABASE < "$SQL_FILE"
    echo "$TABLE 导入完成!"
  else
    echo "找不到 $SQL_FILE, 跳过该表."
  fi
done

echo "所有表导入完成!"
