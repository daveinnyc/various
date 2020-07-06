// Create a fake print function

function print(){
    for (var i = 0; i < arguments.length ; i++){
        document.write(String(arguments[i]))
    }
    document.write("<br>");
}


function testPrint(){
    print("oneString");
    print("one String with spaces");
    print();
    print("oneString", " twoString");
    print(["a", "b", "c"]);
    print(1, 2, 3);
    print(1, " x ", 2, " y");
}

testPrint();