1. **BEFORE FIELD l_txt**：
   - 在用户与字段 `l_txt` 交互之前触发。
   - 适用于进行输入验证或初始化操作。
2. **AFTER FIELD l_txt**：
   - 在用户与字段 `l_txt` 交互之后触发。
   - 适用于处理数据更新或进行额外的计算。
3. **ON CHANGE l_txt**：
   - 当字段 `l_txt` 的值发生变化时触发。
   - 适用于在数据变化时执行实时更新或逻辑操作。
4. **ON ACTION controlp INFIELD l_txt**：
   - 当用户在字段 `l_txt` 上触发特定动作（如按下一个按钮 `controlp`）时触发。
   - 适用于在特定操作上响应字段事件。