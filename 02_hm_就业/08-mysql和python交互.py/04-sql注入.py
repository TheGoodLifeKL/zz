from pymysql import connect 

class JD(object):
    def __init__(self):
         # 创建Connection连接
        self.conn = connect(host='localhost',port=3306,database='jingdong',user='root',password='mysql',charset='utf8')
        # 获得Cursor对象
        self.cursor = self.conn.cursor()
    def __del__(self):
        # 关闭cursor对象
        self.cursor.close()
        self.conn.close()
    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)
        
    def show_all_items(self):
       # 显示所有商品
        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_all_cates(self):
        # 显示所有商品分类
        sql = "select name from goods_cates;"
        self.execute_sql(sql)

    def show_all_brands(self):
        # 显示所有商品品牌分类
        sql = "select name from goods_brands;"
        self.execute_sql(sql)
    def add_brands(self):
        item_name = input("请输入要添加的商品品牌名字:")
        sql = """insert into goods_brands (name) values("%s")""" % item_name
        self.cursor.execute(sql)
        self.conn.commit()
    def get_info_by_name(self):
        find_name = input("请输入要查询的商品名字:")
        # sql = "select * from goods where name = '%s';" % find_name
        # print("--------->%s<---------" % sql)
        # self.execute_sql(sql)
        sql = "select * from goods where name=%s"
        self.cursor.execute(sql, [find_name])
        print(self.cursor.fetchall())


    @staticmethod
    def print_menu():
        print("-----京东商城----")
        print("1: 所有商品")
        print("2: 所有的商品分类")
        print("3: 所有的商品品牌分类")
        print("4: 添加一个商品品牌分类")
        print("5: 根据一个名字查询商品")
        num = input("请输入功能序列号:")
        return num

    def run(self):
        while True:
            num = self.print_menu()    
            if num == "1":
                # 查询所有商品
                self.show_all_items()
            elif num == "2":
                # 查询所有商品分类
                self.show_all_cates()
            elif num == "3":
                # 查询所有商品品牌分类
                self.show_all_brands()
            elif num == "4":
                # 添加一个商品品牌
                self.add_brands()
            elif num == "5":
                # 根据名字查询商品
                self.get_info_by_name()
            else:
                print("输入有误,请重新输入")
def main():
    # 1 创建一个京东商城对象
    jd = JD()
    # 2 调用run
    jd.run()


if __name__ == "__main__":
    main()
