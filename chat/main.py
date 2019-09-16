#!/usr/bin/env python

import os
import logging   #打印日志
#logging.debug(‘调试’) 蓝色
#looging.info（‘信息’） 绿色
#looging.warning（‘警告’）黄色
#looging.error（'错误'）橙色
#looging.fatal(‘致命错误’) 红色

import tornado.web
import tornado.ioloop
from tornado.options import define, options, parse_command_line

from views import MainHandler,ChatSocketHandler

define("host", default='10.11.55.17', help="地址", type=str)
define("port", default=8000, help="端口", type=int)


def main():
    parse_command_line()

    web_app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/chatsocket", ChatSocketHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "statics"),
    )
    web_app.listen(options.port, options.host)

    logging.info('Server running on %s:%s' % (options.host, options.port))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()





