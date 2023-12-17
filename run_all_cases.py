import os
import pytest

current_path = os.path.dirname(os.path.abspath(__file__))
# json report path
json_report_path = os.path.join(current_path,'reports/json')
# html report path
html_report_path = os.path.join(current_path,'reports/html')

pytest.main(['-s','-v','--alluredir=%s'%json_report_path,'--clean-alluredir'])
# html report
os.system('allure generate %s -o %s --clean'%(json_report_path,html_report_path))
