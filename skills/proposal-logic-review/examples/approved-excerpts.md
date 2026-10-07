# 当前确认稿的中英文节选

以下按原 DOCX 段落提取，作为写作范例，而不是本次重新审核后的科研结论。省略申请人署名和个人演示链接段；其余选入段落保留原文措辞。编号 Pxx 是原 DOCX 零起始段落编号，便于定位。段落在 Markdown 中展示，不代表重新排版后的页数。

文中 [1]—[11] 沿用已确认稿，下方附原稿书目快照。本次没有外部核验其最新版本或发表状态；引用到新的 proposal 前，应按需要重新核对来源。

# 中文节选

<!-- CN P00 -->
## 城市街道激光—视觉三维高斯重建的观测—表征容量匹配研究

<!-- CN P02 -->
## 第一页  |  研究背景、现状与科学问题

<!-- CN P03 -->
### 1. 研究背景与目标

<!-- CN P04 -->
城市数字孪生需要兼顾几何精度与新视角外观真实感的三维底座，以支持空间量测与实景呈现。然而，重建时间与计算资源开销制约了大范围街道场景的规模化构建，如何在有限资源下兼顾质量与效率，是实现低成本重建的关键问题。本研究以已有的配准 LiDAR 点云与多视角影像为输入，旨在保持几何精度和新视角外观质量的同时，提高数据处理与重建优化效率，为城市数字孪生提供低成本、可规模化构建的三维环境。

<!-- CN P05 -->
### 2. 研究现状与问题分析

<!-- CN P06 -->
三维高斯溅射（3DGS）通过显式基元表达几何与外观，支持高质量实时新视角渲染，为上述目标提供了可行路线[1]。围绕其大场景应用，已有研究取得了三方面进展。

<!-- CN P07 -->
（1）大场景规模。LetsGo[2]在 LiDAR 辅助的车库重建中结合空间分块训练与多细节层次表示；Hierarchical 3DGS[3]以 SfM 点云初始化，通过分块训练和层级渲染处理大型地面场景。这些方法通过组织训练与渲染缓解资源压力，证明了大型场景重建的可行性。

<!-- CN P08 -->
（2）几何引导的表示与质量。Structured-Li-GS[4]以体素采样生成锚点，利用 LiDAR 表面法向组织高斯形状，并通过几何约束获得较紧凑且渲染质量有竞争力的表示。GTLR-GS[5]依据曲率与局部颜色变化分配初始高斯，结合几何引导细化与深度监督改善新视角质量，体现了几何与纹理共同指导表示的价值。

<!-- CN P09 -->
（3）训练成本与加速。密集点云若转化为大量高斯，会增加参数更新与存储负担。Chen 等的 Li-GS[6]采用图像特征引导的点云降采样并限制球谐函数（SH）阶数，研究质量与资源需求的取舍；Taming 3DGS[7]和 FastGS[8]通过参数处理与冗余计算优化加速训练。在输入利用方面，基于频率的视图选择[9]估计候选视角的信息增益，优视摄影测量[10]依据可观测性与观测几何优选视角，说明效率提升还需要判断哪些观测值得使用。

<!-- CN P10 -->
现有研究已从大场景组织、几何引导和训练加速三个层面改善质量与效率，但仍需建立随局部表面与观测条件变化的协同配置依据。在给定质量要求下，如何联系输入选择、高斯容量和参数更新，判断哪些配置必要、哪些投入收益有限，仍需进一步研究。本项目据此探索有效观测、局部表示与优化投入的匹配关系，以减少逐场景试配与不必要的计算。

<!-- CN P11 -->
### 3. 拟解决的关键科学问题

<!-- CN P12 -->
（1）有效观测与局部高斯表征的匹配规律：达到目标质量，需要哪些输入与高斯配置？研究表面的几何与纹理需求、观测覆盖和可靠性，如何共同决定必要输入与表示。通过增减观测、高斯数量及外观自由度，揭示质量变化与收益饱和规律，区分观测不足、表示不足和继续投入收益有限的条件，为高斯数量、空间分布、形状及外观能力提供质量约束下的配置依据。

<!-- CN P13 -->
（2）几何—外观先验对初始化与收敛的作用机制：怎样利用已有信息，减少达到目标质量所需的优化？在明确局部表示需求后，研究 LiDAR 几何与多视图外观先验如何影响高斯初值、必要参数自由度和收敛代价。厘清先验可信度、初始形状与分布、几何约束和参数更新之间的关系，判断哪些结构可提前确定、哪些参数仍需调整，以合理初值与按需优化减少开销，同时避免过强约束固化误差或过弱约束引起几何漂移。

<!-- CN P14 -->
第一问确定足够的观测与表示配置，第二问研究如何以更低成本实现该表示。共同目标是在保持几何精度和新视角质量的条件下，降低输入处理、初始化与训练的总成本。

<!-- CN P15 -->
## 第二页  |  研究方法、验证与预期成果

<!-- CN P16 -->
第一项让影响因素能够被区分；第二项回答“需要怎样的输入与表示”；第三项回答“怎样利用先验减少实现该表示的优化成本”。

<!-- CN P17 -->
### 1. 面向机制分析的可控仿真与观测实验

<!-- CN P18 -->
参考 LiteReality 的可编辑场景构建思路[11]，以实测 LiDAR 与多视角影像为约束，利用视觉语言模型辅助 Blender 脚本，构建几何受测量约束、外观近似真实、规模可调的结构化场景。独立网格渲染与激光射线模拟提供已知几何、相机和可见性信息。仿真用于独立控制真实重复采集中难以分离的因素，其真值对应所构建场景。

<!-- CN P19 -->
在同一场景中分别改变影像密度、视角覆盖、观测质量、点云采样与高斯容量，并控制几何与纹理变化以研究关键交互。输入点云与可训练高斯独立控制，重建只使用各组规定的观测。设置统一优化条件及必要的延长优化对照，区分信息、表示和收敛限制，为匹配关系识别提供可重复证据。

<!-- CN P20 -->
### 2. 表面级有效观测评价与高斯联合配置

<!-- CN P21 -->
以局部连通表面建立观测—高斯表示—区域质量与成本的对应关系。通过平面提取、区域生长和邻接可靠性检查，区分可靠平面、连续平缓的残余表面及复杂或不确定区域，为采样和表示提供候选方式。保留各实验允许使用的几何参考云，并单独配置高斯中心云。

<!-- CN P22 -->
结合表面结构与纹理、影像清晰度、有效分辨率、角度覆盖和互补性，拟建立条件化质量—成本响应模型，比较不同输入与高斯配置，形成候选充分性条件和可执行规则：保留哪些观测、怎样采样中心，以及需要何种数量、分布、形状和外观能力。通过移除或补充观测与容量检验实际贡献；对比统一配置、仅观测筛选、仅表示配置与联合配置。规则在开发场景确定后固定，用于独立场景。

<!-- CN P23 -->
### 3. 先验引导初始化与状态驱动的按需优化

<!-- CN P24 -->
依据配置结果，利用可靠 LiDAR 表面与多视图纹理初始化高斯位置、方向和尺度。前期稳定几何、覆盖与基元分布，同时拟合基础颜色和不透明度；随后依据观测支持、几何稳定性和持续外观残差，决定参数更新范围、频率及高阶 SH 激活时机。对稳定几何减少调整，对需修正区域保留有界更新与适当约束；在表示不足且观测充分时，研究预算约束下的贴面增密与剪枝。结合视图可见性和渲染贡献，减少候选高斯处理与无效更新。

<!-- CN P25 -->
初始化在匹配输入与预算下单独比较；调度在相同初值下对比固定时间表、统一低阶外观与状态驱动更新。容量调整和可见性筛选另作对照，检验配置依据与按需更新能否降低达到同一质量的成本。

<!-- CN P26 -->
### 4. 访问期间安排和预期成果

<!-- CN P27 -->
访问安排。第1—2个月完成可编辑仿真场景与受控数据集，分析观测覆盖、点云密度与高斯容量的关系；第3—4个月开发几何—纹理协同初始化、分阶段优化与特征监督；第5—6个月完成预算受控的增密对照、真实场景验证和论文整理。采用独立测试视角与参考几何，在相同质量和相同资源下比较细节表现、总耗时及显存开销。

<!-- CN P28 -->
实验条件。主要使用 Google Colab 云端 GPU 与申请人自备笔记本电脑，并使用 Codex 辅助代码开发。本地完成数据整理、场景编辑与结果分析，训练和较大规模渲染按需在云端执行，并依据实际可用算力控制实验规模。

<!-- CN P30 -->
预期成果。形成关于“何为高质量且紧凑的三维场景表征”的可解释经验规律与配置准则，明确不同结构、纹理与观测条件下所需的有效输入、高斯数量、形状与分布，以及相应的优化方式和适用范围；交付可复现实验数据、算法原型和论文稿。研究有望为前馈3D高斯的表示设计与容量分配、自动驾驶及车载移动测量系统（MMS）数据的激光—图像多源融合重建提供理论与实验依据，并支持城市数字孪生及具身智能视觉仿真评测所需的真实尺度、可渲染环境。

# English excerpts

<!-- EN P00 -->
## Observation–Representation Capacity Matching forLiDAR–Visual 3D Gaussian Reconstruction of Urban Streets

<!-- EN P02 -->
## PAGE 1  |  BACKGROUND, STATE OF THE ART AND RESEARCH QUESTIONS

<!-- EN P03 -->
### 1. Background and objective

<!-- EN P04 -->
Urban digital twins require a 3D spatial foundation combining geometric accuracy and realistic novel-view appearance for spatial measurement and visual presentation. Reconstruction time and computational resources constrain large-scale street-scene construction, making quality-preserving efficiency essential under limited resources. Using already registered LiDAR point clouds and multi-view images, this project aims to improve data processing and reconstruction optimization while maintaining geometric and novel-view quality, enabling lower-cost, scalable 3D environments for urban digital twins.

<!-- EN P05 -->
### 2. State of the art and problem analysis

<!-- EN P06 -->
3D Gaussian Splatting (3DGS) represents geometry and appearance with explicit primitives and supports high-quality, real-time novel-view rendering [1], providing a viable route towards this objective. Relevant progress spans three areas.

<!-- EN P07 -->
(1) Large-scene scale. LetsGo [2] combines spatially partitioned training and levels of detail for LiDAR-assisted garage reconstruction. Hierarchical 3DGS [3] uses SfM initialization, chunked training and hierarchical rendering for large ground-level scenes. Both mitigate resource pressure through training and rendering organization, establishing the feasibility of large-scene reconstruction.

<!-- EN P08 -->
(2) Geometry-guided representation and quality. Structured-Li-GS [4] uses voxel-sampled anchors, LiDAR-normal-aligned shapes and geometric constraints to obtain compact representations with competitive rendering quality. GTLR-GS [5] allocates initial Gaussians using curvature and local colour variation, then applies geometry-guided refinement and depth supervision to improve novel views. These methods demonstrate the value of jointly using geometric and appearance cues.

<!-- EN P09 -->
(3) Training cost and acceleration. Converting dense point clouds into many Gaussians increases parameter-update and storage demands. Chen et al.’s Li-GS [6] combines image-feature-guided downsampling with restricted spherical-harmonic (SH) order to address quality–resource trade-offs. Taming 3DGS [7] and FastGS [8] accelerate parameter processing and reduce redundant computation. Frequency-based view selection [9] estimates information gain, while optimized views photogrammetry [10] selects viewpoints using observability and viewing geometry, highlighting the importance of useful observations.

<!-- EN P10 -->
Together, these methods address scene organization, geometry-guided representation and training efficiency, but further evidence is needed to coordinate configurations as local surfaces and observations change. This project investigates which input selections, Gaussian capacities and parameter updates are sufficient at a target quality, linking effective observations to representation and optimization requirements to reduce scene-specific trial and error and unnecessary computation.

<!-- EN P11 -->
### 3. Key scientific questions

<!-- EN P12 -->
RQ1—Observation–representation matching: which inputs and Gaussian configurations are necessary to reach target quality? How do geometric/texture demand, observation coverage and reliability jointly determine sufficient evidence and representation? Controlled changes to observations, Gaussian counts and appearance freedom will reveal quality responses and diminishing returns. The aim is to distinguish observation-limited, representation-limited and saturated conditions, providing quality-constrained rules for Gaussian number, distribution, shape and appearance capacity.

<!-- EN P13 -->
RQ2—Prior-guided initialization and convergence: how can available information reduce the optimization required? Given local representation needs, how do LiDAR geometry and multi-view appearance priors affect initialization, necessary parameter freedom and convergence cost? I will study the interaction of prior confidence, initial shapes and distributions, geometric constraints and updates to identify what can be determined beforehand and what still requires adjustment, reducing work while preserving appearance expressiveness. I will assess when constraints lock in prior errors or allow geometric drift.

<!-- EN P14 -->
RQ1 determines sufficient evidence and representation; RQ2 asks how to realize that representation at lower cost. The common objective is lower total input-processing, initialization and training cost while maintaining geometric and novel-view quality.

<!-- EN P15 -->
## PAGE 2  |  METHODS, VALIDATION AND EXPECTED OUTCOMES

<!-- EN P16 -->
The first method separates the influencing factors; the second asks what inputs and representations are needed; the third asks how priors can reduce the optimization cost of realizing that representation.

<!-- EN P17 -->
### 1. Controlled simulation and observation experiments

<!-- EN P18 -->
Following LiteReality’s editable-scene approach [11], a vision-language model will assist Blender scripting to construct scalable, structured scenes constrained by measured LiDAR geometry and multi-view appearance. Independent mesh rendering and LiDAR ray casting will provide known geometry, cameras and visibility. Simulation enables control that repeated real capture cannot readily provide; its ground truth describes the authored scene.

<!-- EN P19 -->
Within each scene, image density, viewpoint coverage, observation quality, point sampling and Gaussian capacity will vary independently, with controlled geometry/texture changes for key interactions. Input point density and trainable Gaussians will be controlled separately; reconstruction receives only each experiment’s allowed observations. Common optimization settings and selected extended-training controls will distinguish information, representation and convergence limits.

<!-- EN P20 -->
### 2. Surface-level observation assessment and joint configuration

<!-- EN P21 -->
Locally connected surfaces will link observations, Gaussian representations, regional quality and cost. Plane extraction, region growing and adjacency checks will distinguish reliable planes, continuous smooth residual surfaces, and complex or uncertain regions, providing candidate sampling/representation choices. Each experiment’s permitted geometry-reference cloud will be retained separately from its Gaussian-centre cloud.

<!-- EN P22 -->
A conditional quality–cost response model will combine structure, texture, image sharpness, effective resolution, angular coverage and complementary observations. Comparing input–capacity combinations will yield candidate sufficiency conditions and executable rules for observation selection, centre sampling, Gaussian number, distribution, shape and appearance capacity. Removing or adding observations and capacity will test actual contributions. Uniform configuration, observation-only selection, representation-only allocation and joint configuration will be compared. Rules will be fixed on development scenes before independent evaluation.

<!-- EN P23 -->
### 3. Prior-guided initialization and state-dependent optimization

<!-- EN P24 -->
The selected configuration will be initialized using reliable LiDAR surfaces and multi-view texture to set positions, orientations and scales. Early optimization will stabilize geometry, coverage and primitive distribution while fitting basic colour and opacity. Observation support, geometric stability and persistent appearance residuals will then determine update scope, frequency and higher-order SH activation. Stable geometry receives fewer updates; regions needing correction retain bounded adjustments and geometric constraints. Where observations are sufficient but representation remains inadequate, budgeted surface-constrained densification and pruning will be investigated. View-dependent visibility and rendering contribution will reduce candidate processing and unproductive updates.

<!-- EN P25 -->
Initialization will be tested separately with matched inputs and budgets. Given identical initial representations, scheduling tests will compare fixed timetables, uniformly low-order appearance and state-dependent updates. Capacity changes and visibility selection will be separately ablated, testing whether evidence-based configuration and selective updates lower the cost of reaching the same quality.

<!-- EN P26 -->
### 4. Visit plan and expected outcomes

<!-- EN P27 -->
Visit schedule. Months 1–2 will establish editable scenes and controlled data to analyse observation coverage, point density and Gaussian capacity. Months 3–4 will develop geometry–texture initialization, staged optimization and feature supervision; months 5–6 will compare budget-controlled densification, validate real scenes and prepare a manuscript. Independent test views and reference geometry will support fixed-quality and fixed-resource comparisons of detail, total runtime and memory.

<!-- EN P28 -->
Experimental resources. Google Colab GPUs and my own laptop will support experiments, with Codex assisting development. Data preparation, scene editing and analysis will run locally; training and larger rendering jobs will run in the cloud as needed, with scope matched to available compute.

<!-- EN P30 -->
Expected outcomes. The project aims to establish empirical principles for high-quality, compact 3D representations, relating surface and observation conditions to effective inputs, Gaussian configurations and optimization needs. Outputs include configuration rules, reproducible data, algorithm prototypes and a manuscript. Findings could inform feed-forward 3DGS representation and capacity design, and autonomous-driving and mobile-mapping (MMS) LiDAR–image reconstruction, providing theoretical and experimental foundations for metric-scale, renderable environments supporting urban digital twins and embodied-AI visual simulation evaluation.

# 原稿参考文献快照

仅用于解释上述编号，不宣称其最新状态已经重新核实。

[1] B. Kerbl, G. Kopanas, T. Leimkühler, and G. Drettakis. 3D Gaussian Splatting for Real-Time Radiance Field Rendering. ACM Transactions on Graphics, 42(4), Article 139, 2023.
https://doi.org/10.1145/3592433

[2] J. Cui et al. LetsGo: Large-Scale Garage Modeling and Rendering via LiDAR-Assisted Gaussian Primitives. ACM Transactions on Graphics, 43(6), Article 172, 2024.
https://doi.org/10.1145/3687762

[3] B. Kerbl, A. Meuleman, G. Kopanas, M. Wimmer, A. Lanvin, and G. Drettakis. A Hierarchical 3D Gaussian Representation for Real-Time Rendering of Very Large Datasets. ACM Transactions on Graphics, 43(4), 2024.
https://arxiv.org/abs/2406.12080

[4] H. Weng, H. Li, and C. M. Yeum. Structured-Li-GS: Structured 3D Gaussians Splatting with LiDAR Incorporation and Spatial Constraints. ISPRS Annals, XI-2-2026:375–383, 2026.
https://doi.org/10.5194/isprs-annals-XI-2-2026-375-2026

[5] Y. Fang, J. Ge, and J. Xiao. GTLR-GS: Geometry-Texture Aware LiDAR-Regularized 3D Gaussian Splatting for Realistic Scene Reconstruction. arXiv:2603.23192, 2026 (preprint).
https://arxiv.org/abs/2603.23192

[6] W. Chen, R. Zhong, K. Wang, and D. Xie. Li-GS: a fast 3D Gaussian reconstruction method assisted by LiDAR point clouds. Big Earth Data, first published online 2025.
https://doi.org/10.1080/20964471.2025.2479428

[7] S. S. Mallick, R. Goel, B. Kerbl, F. V. Carrasco, M. Steinberger, and F. De La Torre. Taming 3DGS: High-Quality Radiance Fields with Limited Resources. SIGGRAPH Asia Conference Papers, 2024.
https://doi.org/10.1145/3680528.3687694

[8] S. Ren, T. Wen, Y. Fang, and B. Lu. FastGS: Training 3D Gaussian Splatting in 100 Seconds. arXiv:2511.04283, 2025 (preprint version).
https://arxiv.org/abs/2511.04283

[9] M. M. Q. Li, P.-Y. Lajoie, and G. Beltrame. Frequency-based View Selection in Gaussian Splatting Reconstruction. arXiv:2409.16470, 2024 (preprint).
https://arxiv.org/abs/2409.16470

[10] 李清泉，邵成立，万剑华，王海银，姜三，于文率。 优视摄影测量与泛在实景三维数据采集：以实景三维青岛为例。 武汉大学学报（信息科学版），47(10)：1587–1597，2022。
https://doi.org/10.13203/j.whugis20220079

[11] Z. Huang, X. Wu, F. Zhong, H. Zhao, M. Nießner, and J. Lasenby. LiteReality: Graphics-Ready 3D Scene Reconstruction from RGB-D Scans. Advances in Neural Information Processing Systems (NeurIPS), 2025.
https://arxiv.org/abs/2507.02861
