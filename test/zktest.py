import sys
from kazoo.client import KazooClient


def main():
    # noinspection PyStatementEffect
    try:

        nodePath = "/hunteron"
        host = "172.30.10.186"
        port = "2181"
        timeout = 100
        zkc = KazooClient(hosts=host + ':' + port, timeout=timeout)
        zkc.start()

        # 判断节点是否存在
        # if zkc.exists(nodePath + "/test111"):
        #     print(nodePath + "/test111", "存在")
        # else:
        #     # 建立节点，成功后返回新节点路径
        #     childrenPath = zkc.create(nodePath + "/test111", "test111")
        #     print("创建节点：", childrenPath, "成功。")
        #     # 创建临时节点，连接断开则节点自动删除
        #     zkc.create(nodePath + "/test999", "test999", ephemeral=True)
        print(1)
        # 获取节点数据和节点数据，返回2个值，一个是节点数据，一个是节点stat，这是个ZnodeStat对象，它其实是节点属性，一共有12个属性
        node = zkc.get_children('/')
        print("get",node)
        print(1)
        dataAndStat = zkc.get(nodePath)
        data = dataAndStat[0]
        print("数据为：", data)
        stat = dataAndStat[1]
        print("数据版本号为：", stat.version)
        print("数据长度为：", stat.data_length)
        print("子节点数量：", stat.numChildren)

        # 更新节点数据,数据最大为1MB超过则报错，成功后返回 ZnodeStat 对象
        stat = zkc.set(nodePath, value="test222")
        print("数据版本号为：", stat.version)

        # 删除节点，后面的参数用于控制是否递归删除，默认是False,但是这样就会有一个问题，如果该节点下有子节点则本次删除失败，你需要先删除
        # 它下面的所有子节点才行
        # if zkc.exists(nodePath + "/test111"):
        #     result = zkc.delete(nodePath + "/test111", recursive=False)
        #     if result:
        #         print("删除节点成功。")

        print(nodePath + " 的子节点为：", zkc.get_children(nodePath))

        zkc.close()
        zkc.stop()
    except Exception as err:
        print(err.message)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    finally:
        sys.exit()
