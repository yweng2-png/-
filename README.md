# Recycling Demand Forecasting — MSBA Practicum Project (Sponsor: PROMESA)

**作者**: Yujia Weng (William Weng) | Santa Clara University, Leavey School of Business — MS Business Analytics
**项目周期**: 2026年1月 – 2026年6月 | 加州圣克拉拉

## 项目背景

与回收服务公司 **PROMESA** 合作的 MSBA 实践项目，基于 56 家企业、132 所学校、61 家咖啡馆近 3 年的月度回收交易数据，构建预测模型，帮助客户从**固定排班模式**转向**基于回收量的动态调度模式**。

## 我的角色与工作内容

- **数据清洗与整合**：使用 Python（Pandas）处理 249 家合作方的月度回收数据，处理缺失值、按第 95 百分位阈值处理异常值
- **预测建模**：构建 6 个月滑动窗口线性回归模型，预测下月回收量
- **分类建模与模型选择**：使用 `pd.qcut()` 将回收量离散化为高/中/低三级，对 Softmax 回归、XGBoost、随机森林进行基准测试
- **数据可视化**：使用 Matplotlib 制作时间序列趋势图、实际值 vs 预测值散点图、模型对比图
- **商业成果设计**：主导设计三级分类预警系统，将取件规划从固定排班转变为动态调度；针对企业/学校/咖啡馆不同合作方类型提出差异化服务策略
- **利益相关方沟通**：向赞助公司高管及学术导师做最终陈述

## 核心成果

| 指标 | 结果 |
|---|---|
| 企业数据集回归模型 | R² = 0.853 |
| 咖啡馆数据集回归模型 | R² = 0.88 |
| 学校数据集回归模型 | R² = 0.334（受限于历史数据不足，需分类方法而非精确数值预测） |
| Softmax 分类模型 | 准确率 / F1 ≈ 73.7% |

## 文件说明

- [`Yujia Business Data Analysis-Copy1(1).ipynb`](./Yujia%20Business%20Data%20Analysis-Copy1(1).ipynb) — 完整数据清洗、建模与可视化代码（Jupyter Notebook，可直接在网页查看）
- [`Final_Presentation.pdf`](./Final_Presentation.pdf) — 项目最终汇报讲稿（PDF，可在线预览）

## 技术栈

Python (Pandas, NumPy, Scikit-learn, Matplotlib) · SQL · Softmax Regression · XGBoost · Random Forest · Feature Engineering · EDA

## 联系方式

📧 yweng2@scu.edu | 🔗 [LinkedIn](https://www.linkedin.com/in/william-weng-083ba9402)
