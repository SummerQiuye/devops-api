from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
import configparser

cg = configparser.RawConfigParser()
cg.read("config.ini", encoding="UTF-8")
cookie = cg.get("web", "cookie")
new = eval(cookie)

print(new)


class TestCaseLoginAndCreat(HttpRunner):

    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("")
            .post("")
            .with_headers(
                **{
                    }
            )
            .with_cookies(
                **new

            )
            .with_data(
                {"phone": "18710748230", "password": "123456", "remember": "true"}
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
        ),
        Step(
            RunRequest("创建文件，获取一个随机docId，并作为入参传入下一个接口")
            .post("https://api2.mubu.com/v3/api/list/create_doc")
            .with_headers(
                **{
                    "Host": "api2.mubu.com",
                    "Connection": "keep-alive",
                    "Content-Length": "25",
                    "Accept": "application/json, text/plain, */*",
                    "Jwt-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTE2MjM5NTEiLCJleHAiOjE2MjA0MDAxOTMsImlhdCI6MTYxNzgwODE5M30.cCLeXbGv8bBcbjAjywGUbjQA_vFdtR6RgazmAWnW9RETKno_y1qpMCPek0-y9UJnatbohr_wBQh0EkjfCCwNAw",
                    "Content-Type": "application/json;charset=UTF-8",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
                    "data-unique-id": "5af8ec14-0e06-45fb-948e-5852d15f593a",
                    "x-request-id": "3ea699c8-c82f-4fe9-9a0a-e7c611dec3d8",
                    "version": "3.0.0.21310",
                    "Origin": "https://mubu.com",
                    "Sec-Fetch-Site": "same-site",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://mubu.com/",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"folderId": "0", "type": 0})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("给创建的文件输入内容")
            .post("https://api2.mubu.com/v3/api/refer/search_refers")
            .with_headers(
                **{
                    "Host": "api2.mubu.com",
                    "Connection": "keep-alive",
                    "Content-Length": "57",
                    "Accept": "application/json, text/plain, */*",
                    "Jwt-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTE2MjM5NTEiLCJleHAiOjE2MjA0MDAxOTMsImlhdCI6MTYxNzgwODE5M30.cCLeXbGv8bBcbjAjywGUbjQA_vFdtR6RgazmAWnW9RETKno_y1qpMCPek0-y9UJnatbohr_wBQh0EkjfCCwNAw",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
                    "data-unique-id": "5af8ec14-0e06-45fb-948e-5852d15f593a",
                    "x-request-id": "278aa778-8931-4dcf-99fe-2ead0d51ff26",
                    "Content-Type": "application/json;charset=UTF-8",
                    "Origin": "https://mubu.com",
                    "Sec-Fetch-Site": "same-site",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://mubu.com/",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"docId": "3PCZY46pa3_", "keywords": "zhangtong", "option": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
    ]


# if __name__ == "__main__":
#     TestCaseLoginAndCreat().test_start()