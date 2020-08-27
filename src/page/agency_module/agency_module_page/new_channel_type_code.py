#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 21:06
# @Author: fyl
# @File : new_channel_type_code.py  渠道类型码新增
from config.global_var import sleep
from src.page.agency_module.agency_module_page.common_page import CommonPage
from src.utils.log import info


class NewChannelTypeCode(CommonPage):
    upper_agent_type = "//*[@id='upperAgentType']"  # 三级渠道类型
    agent_type = "//*[@id='agentType3']"    # 渠道类型码
    agent_type_name = "//*[@id='agentTypeName3']"
    submit_list_file_btn = "//*[@id='submitListFileBtn']"   #确定
    sap_agent_type_name = "//*[@id='saPAgentType.agentTypeName']"   # 渠道类型码名称
    permit_no = "//*[@id='saAAgentTypeOtherInfo.permitNo']"   # 许可证机构编码
    img_btn1 = "//*[@id='imgBtn1']"
    save_agent_type = "//*[@id='saveAgentType']"
    save_success = "//body/table/tbody/tr/td[2]"    # 保存成功

    def into_page(self, module_menu):
        self.to_main_page(module_menu, "中介机构", "渠道类型码新增")

    def click_agent_type(self, code):
        '''
        code:渠道类型码
        '''
        self.double_click(self.wait_until_el_xpath(self.upper_agent_type))
        sleep(2)
        self.switch_to_window()
        # 取消选择页面的onbeforeunload
        self.execute_script("window.onbeforeunload = null;")
        info("进入选择渠道类型码："+self.get_head_text())
        self.send_keys(self.wait_until_el_xpath(self.agent_type),code)
        self.click(self.wait_until_el_xpath(self.agent_type_name))
        self.click(self.wait_until_el_xpath(self.submit_list_file_btn))
        sleep(2)
        self.switch_to_window()
        self.select_frame_id(self.frame_id)
        self.select_frame_id(self.iframe_page)
