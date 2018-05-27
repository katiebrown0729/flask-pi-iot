echo removing all the .py files
rm *.py
echo *** getting lastest from master ****
echo accelerometer_post.py_test
curl -OL https://raw.githubusercontent.com/katiebrown0729/flask-pi-iot/master/pi_client/accelerometer_post_test.py > accelerometer_post_test.py
echo accelerometer_post.py
curl -OL https://raw.githubusercontent.com/katiebrown0729/flask-pi-iot/master/pi_client/accelerometer_post.py > accelerometer_post.py
python accelerometer_post_test.py -v