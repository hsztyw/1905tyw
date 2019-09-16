$(document).ready(function() {
    if (!window.console) window.console = {}
    if (!window.console.log) window.console.log = function() {}
//关闭页面控制台，对整个页面和控制台的初始化

    $("#messageform").live("submit", function() {
        newMessage($(this))
        return false
    })
    //live跟on差不多，on表示绑定事件，live也是。
    $("#messageform").live("keypress", function(e) {
       //keypress绑定的摁下的按键，e.keyCode==13表示回车键
        if (e.keyCode == 13) {
            newMessage($(this))
            return false
        }
    })

    $("#message").select()   //表示页面处于选中状态
    updater.start()    //连接websocket
})

function newMessage(form) {
    var message = form.formToDict()
    updater.socket.send(JSON.stringify(message))
    $("#message").val("").select();
}
//发送的新消息，定位到的form表单，select表示焦点不变

jQuery.fn.formToDict = function() {
    var fields = this.serializeArray()
    var json = {}
    for (var i = 0; i < fields.length; i++) {
        json[fields[i].name] = fields[i].value
    }
    if (json.next) delete json.next
    return json
}

function add(id, txt) {
    var ul = $("#user_list")
    var li = document.createElement("li")
    li.innerHTML = txt
    li.id = id
    ul.append(li)
}

function del(id) {
    $("#" + id).remove()
}

var updater = {
    socket: null,
//定义一个空值
    start: function() {
        var url = "ws://" + location.host + "/chatsocket"  //对应main里的路由
        updater.socket = new WebSocket(url)     //连接网络
        updater.socket.onmessage = function(event) {
            updater.showMessage(JSON.parse(event.data))   //调用showMessage
        }
    },

    showMessage: function(message) {
        del(message.client_id)
        if (message.type != "offline") {    //判断是否是离线消息
            add(message.client_id, message.username)
            if (message.body == "") return   //如果为空
            var existing = $("#m" + message.id)   //定位message.id
            if (existing.length > 0) return
            var node = $(message.html)
            node.hide()
            $("#inbox").append(node)
            node.slideDown()    //消息向下滚动
        }
    }
}


//type就是元类，class底层都是由type来创建的
//