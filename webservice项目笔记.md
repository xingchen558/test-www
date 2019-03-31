## 如何完成接口实战项目？
* 充分了解项目需求：每个接口的功能，逻辑，依赖关系，数据结构特点等
* 了解接口协议特点: web service ? 如何请求？如何构造入参？，如何解析出参？
* 根据项目特点设计框架：可读性，可维护性，可扩展性
  如何结构分层？数据层，用例层，逻辑层
  如何封装？按照功能封装，do_excel, read_conf,db_tools,context,log....

#### 如何请求web service 接口：工具 ：soapUI， Python 库 ：suds
```python
import json

import suds
from suds.client import Client

def request(url, function_name, datas):
    '''

    :param url:
    :param function_name:
    :param datas:
    :return:

    '''
    print('请求的URL：{0}'.format(url))
    print('请求的function_name：{0}'.format(function_name))
    print('请求的datas：{0}'.format(datas))
    if type(datas) == str:  # 入参必须是字典，所以增加判断，如果不是字典，就转成字典
        datas = json.loads(datas)
    # 根据suds调用方式，编写好表达式
    s = "Client('{0}').service.{1}({2})".format(url, function_name, datas)
    try:
        resp = eval(s)  # 巧用eval函数，动态编译执行
        print('响应信息:', resp.retInfo)  # 获取正常响应
        return resp.retInfo
    except suds.WebFault as ex:
        print('错误信息:', ex.fault.faultstring)  # 获取错误信息
        return ex.fault.faultstring


if __name__ == '__main__':
    send_mc_url = 'http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl'
    datas = {'client_ip': '127.0.0.2', 'tmpl_id': 1, 'mobile': 15810447656}
    # 发送短信验证码
    request(send_mc_url, 'sendMCode', datas)
    # 注册
    other_url = 'http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl'
    datas = {'verify_code': '', 'user_id': 'mongo', 'channel_id': 1, 'pwd': '123456', 'mobile': '15810447656'}
    request(other_url, 'userRegister', datas)
    # 实名认证
    datas = {'uid': '100005221', 'true_name': 'mongo', 'cre_id': '123456789009876543'}
    request(other_url, 'verifyUserAuth', datas)
```

#### 特殊测试数据的构造

* 手机号码的唯一性 【最好保持手机号后三位固定】

  ```python
  雨轩的做法是随机产生，但是后三位固定不变
  import random
  #随机产生手机号，尾号后三位固定不变，但是需要增加一个从数据库里面查询的验证，如果已存在则重新生成！！！
  def creat_mobile():
      second = [3,5,7,8][random.randint(0,3)]
      third = {3:random.randint(0,9), 5:[i for i in range(10) if i !=4][random.randint(0,8)],
               7:[6,7][random.randint(0,1)], 8:random.randint(0,9)}[second]
      # 中间5位随机
      middle = random.randint(9999,100000)
      # 尾号最后3位固定不变
      last_three = 320
      #拼接后的手机号
      return '1{}{}{}{}'.format(second, third, middle, last_three)
  ```

```python
向右转的做法是从固定的库里面获取最大手机号码，然后加1000
def setUp(self): # 每次用例执行前 先查找到库中最大手机号码
    self.sql = 'SELECT * from sms_db_84.t_send_info_0 ORDER BY Fmobile_no DESC LIMIT 1'
    self.max_phone = mysql.fetchone(self.sql)['Fmobile_no']

@data(*cases)
def test_sendMCode(self,case): # 定义一个case变量来接收测试数据
    mobile = int(self.max_phone) + 1000 # 库中最大手机号码+1000 >>>手机号不重复
    setattr(Context,'mobile',str(mobile)) # 动态对mobile赋值未发送验证码的手机号
```

#### 用户名唯一性，身份证号码合法性

```python
王波的做法，随机数
class Get_info():
    first_name=['赵', '钱', '孙', '李', '周', '吴', '郑', '王',
                '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱',
                 '秦', '尤', '许', '何', '吕', '施', '张', '孔', '曹',
                 '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹',
                 '喻', '柏', '水', '窦', '章', '云', '苏', '潘', '葛',
                 '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗',
                 '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍',
                 '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪',
                 '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
                 '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余',
                  '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
                  '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝',
                  '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
                  '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
    last_name=['子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要',
               '她', '出', '也', '得', '里', '后', '自', '以', '会', '家', '可', '下', '而', '过', '天', '去', '能',
                '对', '小', '多', '然', '于', '心', '学', '么', '之', '都', '好', '看',
                '起', '发', '当', '没', '成', '只', '如', '事', '把', '还', '用', '第',
                 '样', '道', '想', '作', '种', '开', '美', '总', '从', '无', '情', '己',
                  '面', '最', '女', '但', '现', '前', '些', '所', '同', '日', '手', '又',
                  '行', '意', '动', '方', '期', '它', '头', '经', '长', '儿', '回', '位',
                  '分', '爱', '老', '因', '很', '给', '名', '法', '间', '斯', '知', '世',
                       '字', '场', '平', '报', '友', '关', '放', '至', '张', '认', '接', '告', '入', '笑',
                       '内', '英', '军', '候', '民', '岁', '往', '何', '度', '山', '觉', '路', '带', '万',
                       '男', '边', '风', '解', '叫', '任', '金', '快', '原', '吃', '妈', '变', '通', '师',
                       '立', '象', '数', '四', '失', '满', '战', '远', '格', '士', '音', '轻', '目', '条',
                        '呢', '病', '始', '达', '深', '完', '今', '提', '求', '清', '王', '化', '空', '业',
                         '思', '切', '怎', '非', '找', '片', '罗', '钱', '紶', '吗', '语', '元', '喜', '曾',
                          '离', '飞', '科', '言', '干', '流', '欢', '约', '各', '即', '指', '合', '反', '题',
                           '必', '该', '论', '交', '终', '林', '请', '医', '晚', '制', '球', '决', '窢', '传',
                           '画', '保', '读', '运', '及', '则', '房', '早', '院', '量', '苦', '火', '布', '品',
                            '近', '坐', '产', '答', '星', '精', '视', '五', '连', '司', '巴', '奇', '管', '类',
                            '未', '朋', '且', '婚', '台', '夜', '青', '北', '队', '久', '乎', '越', '观', '落',
                            '尽', '形', '影', '红', '爸', '百', '令', '周', '吧', '识', '步', '希', '亚', '术',
                            '留', '市', '半', '热', '送', '兴', '造', '谈', '容', '极', '随', '演', '收', '首',
                            '根', '讲', '整', '式', '取', '照', '办', '强', '石', '古', '华', '諣', '拿', '计',
                            '您', '装', '似', '足', '双', '妻', '尼', '转', '诉', '米', '称', '丽', '客', '南',
                            '领', '节', '衣', '站', '黑', '刻', '统', '断', '福', '城', '故', '历', '惊', '脸',
                            '选', '包', '紧', '争', '另', '建', '维', '绝', '树', '系', '伤', '示', '愿', '持']
    """身份证处理类：写死身份证的前后段，只改变出生日期，然后拼接后，根据规则算出最后一位校验码"""
    WI=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2] #每一位对对应加权系数
    begin=[5,1,0,7,8,1]    #省份证开头
    end=[4,2,5]             #省份证最后2到2位
    '''根据算法 算出余数后 根据余数取出ver_code 对应位子的值，改值为身份证最后一位'''
    ver_code=[1,0,"X",9,8,7,6,5,4,3,2]
    def __init__(self):
        self.conf=Read_conf()
        self.birthday=self.conf.get("card_birthday","birthday")
        self.get_birthday_list()
    def get_birthday_list(self):
        birthday_list=[]
        for i in    self.birthday:
            birthday_list.append(int(i))
        self.birthday_list=birthday_list

    def write_new_birthday(self):
        day=self.birthday[6:8]
        month=self.birthday[4:6]
        year=self.birthday[0:4]

        if month=="12":
            if day=="28":
                new_year=str(int(year)+1)
                new_month="01"
                new_day="01"
                new_birthday=new_year+new_month+new_day
            else:
                new_day=str(int(day)+1)
                if len(new_day)==1:
                    new_day="0"+new_day
                new_birthday=year+month+new_day
        else:
            if day=="28":
                new_month=str(int(month)+1)
                if len(new_month)==1:
                    new_month="0"+new_month
                new_day="01"
                new_birthday=year+new_month+new_day
            else:
                new_day=str(int(day)+1)
                if len(new_day)==1:
                    new_day="0"+new_day
                new_birthday=year+month+new_day
        self.conf.write("card_birthday", "birthday", new_birthday )
    def get_card(self):
        card=self.begin+self.birthday_list+self.end
        sum=0
        for i in range(17):
            sum=card[i]*self.WI[i]+sum
        Y_local=sum%11
        last_num=self.ver_code[Y_local]
        card.append(last_num)
        for i in range(len(card)):
            card[i]=str(card[i])
        card="".join(card)
        self.write_new_birthday()
        return card

    def get_name(self):
        first_name=random.choice(self.first_name)
        last_name=random.choice(self.last_name)
        name=first_name+last_name
        return name

```

#### 超时如何处理？

* 显性等待 time.sleep(60)

* 直接使用库里现有的已过期数据


## 学习方法：笔记和思路非常重要，学会如何自己找答案！！





