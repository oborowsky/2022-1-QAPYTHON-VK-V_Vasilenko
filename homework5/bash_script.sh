result=bash_result.txt
echo "Общее количество запросов:" >> @result
wc -l access.log | awk '{print $1}' >> @result
echo "Количество запросов по типу:" >> @result
cat access.log | awk '{print substr($6,2); }' | sort |uniq -c | sort -rn >> @result
echo "Топ 10 самых частых запросов:" >> @result
cat access.log | awk '{print $7}' | sort |uniq -c | sort -rn | head -n 10 >> @result
echo "Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой:" >> @result
cat access.log | awk '{print $1,$9,$10,$7}' | awk '$2~/^4/' | sort -rk 3 | head -n 5 >> @result
echo "Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой:" >> @result
cat access.log | awk '{print $1, $9}' | sort | uniq -c | awk '$3~/^5/' | sort -rnk 1 | awk '{print $1, $2}' | head -n 5 >> @result