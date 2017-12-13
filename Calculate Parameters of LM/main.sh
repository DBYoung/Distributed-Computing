hadoop jar /usr/lib/hadoop-current/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar  -D stream.non.zero.exit.is.failure=false -numReduceTasks 1 \
-file /home/lifeng/pc2017fall/cufe_fengyangyang/matmap.py -mapper "matmap.py" \
-file /home/lifeng/pc2017fall/cufe_fengyangyang/matred.py -reducer "matred.py"  \
-input cufe_fengyangyang/Lab2/data/sdata.csv \
-output cufe_fengyangyang/Lab2/output
