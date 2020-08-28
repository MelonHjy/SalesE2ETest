#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 21:06
# @Author: fyl
# @File : edit_channel_type_code.py  渠道类型码修改
from config.global_var import sleep
from src.page.agency_module.agency_module_page.common_page import CommonPage
from src.utils.log import info


class EditChannelTypeCode(CommonPage):
    upper_agent_type = "//*[@id='upperAgentType']"  # 三级渠道类型
    agent_type = "//*[@id='agentType3']"    # 渠道类型码
    agent_type_name = "//*[@id='agentTypeName3']"
    full_name = "//*[@id='saAAgentTypeOtherInfo.fullName']"
    submit_list_file_btn = "//*[@id='submitListFileBtn']"   #确定
    sap_agent_type_name = "//*[@id='saPAgentType.agentTypeName']"   # 渠道类型码名称
    permit_no = "//*[@id='saAAgentTypeOtherInfo.permitNo']"   # 许可证机构编码
    img_btn1 = "//*[@id='imgBtn1']"
    update_agent_type = "//*[@id='updateAgentType']"
