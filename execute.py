# -*- coding:utf-8 -*-
#@Time : 2020/6/28 16:37
#@Author: fyl
#@File : execute.py
import pytest

if __name__ == '__main__':
    # pytest.main(['-s', 'src/testcase/agent_sales_manage/test_SALES_validate.PY','-m','verify'])
    # pytest.main(['-s', 'src/testcase/agent_sales_manage/test_SALES_YLDLZ_200.PY'])
    # pytest.main(['-s', 'src/testcase/group_issue_manage/test_SALES_YLTD_006.PY'])
    pytest.main(['-s', 'src/testcase/agency_org_manage/test_SALES_YLZJ_009.PY'])