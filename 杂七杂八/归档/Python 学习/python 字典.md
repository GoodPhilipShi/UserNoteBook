- 方法：

  - key in dict：如果键在字典dict里返回true，否则返回false

    ```python
    a = {"a":0,"b":1,"c":2}
    if "a" in a:
        print("在")
    else:
        print("不在")
    --------
    在
    ```

  - dict.items()：以列表返回可遍历的(键, 值) 元组数组。

    ```python
    dict_id = ''('1', {'name': '李强', 'sex': '男', 'age': 18, 'path': 100}), ('2', {'name': '李强', 'sex': '男', 'age': '18', 'path': '100'})'
    dict1 = dict_id.items()
    print(dict_id.items())
    print(list(dict1)[0][0])
    ```

    

