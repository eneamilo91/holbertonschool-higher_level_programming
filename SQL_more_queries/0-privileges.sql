-- script to list privileges
mysql -u root -p'root'

USE mysql;

SELECT * FROM user WHERE User='user_0d_1' AND Host='root';

SELECT * FROM user WHERE User='user_0d_2' AND Host='root';