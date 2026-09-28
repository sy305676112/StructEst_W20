# 为 Pipeline Exposure 的 investment 结果建一个 applied model：计划

*依据：Francois, "How to Build a Political Economy Model"（IGC-BREAD Week 3 slides）；paper draft（Aug 2026）；memo v7（Sep 24, 2026）。*
*配套文件：`model_checks.py` 用 sympy 验证本文所有比较静态的符号与条件（`python3 model_checks.py`，21/21 通过）。*
*引用约定：slides p.x = BREAD slide 编号；memo x/18 = memo 页脚编号；Table/Fig/OA = paper 的编号。*

---

## 0. 一页摘要

**一句话 WHY（可直接用在 paper 里）**

> A pending recognition-or-measurement proposal makes it uncertain how today's investment will show up in the numbers that short-horizon investors and contracts read. A manager who weighs those numbers holds investment back until the reading is known.

**模型骨架（spare parts，slides p.23, 39–40）**：Stein (1989) / Bebchuk–Stole (1993) 的 myopic-manager 架构（manager 在乎短期价格，市场通过报表"读"投资）+ Bernanke (1983) 的 wait-and-see（一个会 resolve 的不确定性）。FASB pipeline 改变的是 *reporting regime 的 law of motion*（pending → resolved），正如 slides 里 reservation 改变的是 *political power 的 law of motion*（p.26）。

**模型带来了什么**（对照 slides p.35 "What did the modelling actually add?"）

1. **一个 benchmark（Lemma 0），它是整个 WHY 的支点。** 如果价格完全理性地看穿报表、manager 风险中性、又不能推迟投资，那么规则的*不确定性*对投资没有任何影响，起作用的只有规则的*预期内容*（anticipation），而且 resolution 时投资平均不会反弹。memo 里的 Resolving 系数（+1.518）拒绝了这个 benchmark（除非 resolution 系统性地是好消息，T2 可以检验）。所以 memo 12/18 里 "with the mapping uncertain, holds back" 这一步，必须由两样东西生成：(i) 报表数字在 *level* 上影响短期价格或合约；(ii) 一个 hold back 的理由：concave 的短期 payoff（variant R），或者推迟的期权（variant W）。
2. **一个非单调预测**：proposal 越 contested（Board 可能两边倒），效应越大，呈 inverted-U。这是 slides p.30–31 里 "contesting jatis" 的对应物。
3. **第二个 comparative static**：reading intensity $\lambda=\omega b$（short-horizon ownership、face-value reading、写在报表数字上的合约）。
4. **一个新变量**：variance-weighted exposure $\sum_p e_{ip}^2\sigma_p^2$。同样的 PE，如果集中在少数 proposal 上，reading risk 更大。这是 slides p.33–34 里 concentration index $H$ 的对应物。
5. **对已有证据的重新解读**：memo 用来排除 learning 的 PE×q > 0，和 real-options 的 catch-up 检验，其实是同一个问题的两面。R 预测 PE×q ≤ 0 且没有 catch-up；W 预测 PE×q > 0 且有 catch-up。目前两者指向相反方向。

**动手之前的三个警示（模型给的 discipline，slides p.12）**

- **模型隐含的 placebo 目前没过。** *No requirement changed* 组件 within-firm 是 −1.411（t = −4.83，OA7）。去掉 2008 Going Concern 一个 proposal，investment 系数就缩小 38.6%，是所有 proposal 中影响最大的（OA6）。在模型里，这两者都不改变投资如何被计量，应该 ≈ 0。
- **Re-exposure 的处理看起来不一致。** 按 Table OA1，同一项目的原 ED 和 re-exposure 常常同时算作 pending：leases 2010-010 与 2013-012；revenue 2010-006 与 2011-011；going concern 2008-019 与 2013-013；income-tax disclosure 2016-010、2019-005 与 2023-001；loss contingencies 2008-010 与 2010-009；transfers 2005-020 与 2008-013（后者标题就是 "Revision of 8/11/05 ED"）；debt classification 2017-001 与 2019-015。正文的退出规则是 "a re-exposure that supersedes it" 结束窗口，Table 1 却只记了 2 个 superseded（都是 EPS）。模型里不确定性的单位是*最终会生效的那条规则*，所以 exposure 应该按 project lineage 计。
- **所以顺序是：先 pre-flight（lineage 修正 + placebo），再用模型解释。** BREAD 的 Step 1 默认事实本身是牢靠的。

**我的建议**：把 W（"wait until the reading is known"）作为主版本，R 作为 robustness variant。理由有三：holding back 在 W 里是生成的，不需要假设风险厌恶；memo 里的高管引语大多在说 "等"；PE×q > 0、redeployability 为正也支持 W。W 的主要反证是 catch-up 不稳健，所以 resolution event study（T2）是第一优先级。paper 里可以写一个同时含 $(\rho,\delta)$ 的模型，让 T2/T6 来裁决。

**第一步（Phase A，全部用现有数据，约 3 周）**：T14 lineage 修正 → T5/T4 placebo → T1 quadratic exposure horse race → T2 resolution event study（按 outcome 和 tone 分组）→ T6 R vs W（q 用 logs 和 levels、redeployability）。

---

## 1. 诊断：paper 现在在哪里

slides 的 applied-modelling 顺序是 Data → Empirical fact → Mechanism → Model → New prediction → New evidence（p.10）。paper 完成了前两步；memo v7 在第三步上迈了一步（选了 market reading）；第四步（Model）还没有。

**已经有的**

- 一个充分验证过的测量：dictionary、comment letters、XBRL、方差分解、measurement error。
- Investment 事实：PE ↑ ⇒ I/K ↓（Table 8 col 3：−1.683，t = −5.00，均值的 3.3%）。
- 分解：R&M 承载全部效应，display/disclosure 为零（Fig 4）；comment-letter uncertainty 承载，attention 不承载（Table 9）。
- memo v7：timing（Active/Resolving/Entering）、ownership gradient、ICC 为零、learning 不成立、real options 不确定，一张 channel 表，最后选了 "market reading"。

**缺的**（用 slides 的标准衡量）

- **"holds back" 没有被推导出来。** memo 12/18 写的是 "with the mapping uncertain, holds back"。但在标准的 real-effects 设定下（理性价格 + 风险中性 manager），mapping 不确定并不导致 hold back（Lemma 0）。WHY 恰好在 "holds back" 这个词上有缺口。这正是 slides p.50 的问题："Is the behaviour actually generated, or have you assumed it?"
- **channel 表（memo 11/18）里的 separating predictions 不是从一个共同的模型推出来的。** 所以它看不出哪些检验其实是同一个问题（q 和 catch-up），也看不出哪些结果应该一起动。
- **两个应用和分解目前只有文字解释。** paper 里的原话是 "Investment responds at the margin that changes what a number will be; pricing responds at the margin that changes what a number tells you"。模型可以把这句话变成一个命题（Prop 3）。

---

## 2. Step 1：模型必须解释的事实（slides p.11）

| # | 事实 | 估计 | 来源 | 建模中的角色 |
|---|---|---|---|---|
| F1 | PE ↑ ⇒ I/K ↓ | −1.683（t = −5.00），均值的 3.3%；memo v7：−1.531 | Table 8；memo 9/18 | motivating |
| F2 | Timing：pending 时下降，resolve 时恢复，issue 时没有额外效应 | Active −1.725；Resolving +1.518（k=0）、+1.385（k=1）；Entering ≈ 0 | memo 10/18 | motivating |
| F3 | Short-horizon owners 放大，dedicated owners 减弱 | PE×transient −1.012；PE×dedicated +0.609；四分位 −0.79 → −3.15 | memo 13–14/18 | motivating |
| F4 | 只有 R&M | R&M −1.823；display −0.247；disclosure +0.172（within firm） | Fig 4 / OA7 | held-out check |
| F5 | Uncertainty 承载，negativity 较弱，attention 不承载 | −1.422 vs 0.044（p = .007）；−1.090 vs −0.156（p = .10）；attention p = .80 | Table 9 | held-out check |
| F6 | Board 的理由：diverse practice 为正 | +0.709；industry-specific −2.073；implementation −1.180；economic conditions −1.131 | OA7 Panel B | held-out check |
| F7 | ICC 没有上升 | composite −1.05bp（t = −0.40）；加入 ICC 后 b(PE) 不变 | memo 16/18 | 区分 cost of capital |
| F8 | 没有 learning；PE×q ≥ 0 | nsync 0.0004；PE×q +0.581（I/K）、+0.651**（total） | memo 17/18 | 区分 learning，**也区分 R 和 W** |
| F9 | Real options 证据弱 | PE×Redeploy +0.413*；catch-up 在 two-way clustering 下 t ≤ 1.43 | memo 18/18 | 区分 R 和 W |
| F10 | ERC 上升 | +0.158/SD（8.8%）；disclosure +0.153，R&M +0.093，display +0.039 | Table 10, Fig 5 | auxiliary（第二个应用） |
| F11 | Exposed firms 写 comment letters | entering PE：基准率的 +24.5% | Table 3 | auxiliary |
| F12 | Placebo 相关 | no requirement changed −1.411（t = −4.83）；去掉 Going Concern 2008 系数缩小 38.6% | OA7, OA6 | 模型要求 ≈ 0 |

两处顺手统一的地方：paper（Aug）和 memo v7（Sep）的系数来自不同版本，写作时统一用一个版本；attention 的差异检验在 5.1.3 节是 p = 0.80，引言写的是 p = 0.92。

建议在 paper 里明说：模型是从 F1–F3 和 pipeline 的制度特征建起来的；F4–F6、F8–F9 不是它调出来的，所以是检验。slides p.15 说得很清楚："If W was not used to construct the model: that prediction is especially informative"。真正的新证据是 §7 的 T1–T15。

---

## 3. Step 2：借机制、拆零件（slides p.23–24, 36, 39–41）

### 3.1 slides 的例子和这篇 paper 一一对应

| Anderson–Francois (2023) | 这篇 paper |
|---|---|
| 母模型：Politics of Fear（Padró i Miquel 2007） | 母模型：Stein (1989) / Bebchuk–Stole (1993) myopia + Bernanke (1983) wait-and-see |
| 保留：group control 的价值 + incumbent 保住控制权的优势 | 保留：manager 对短期价格的权重 $\omega$ + 报表数字进入短期价格 |
| 丢弃：taxation、specialization、patronage | 丢弃：Stein 的 signal-jamming 不动点和 earnings borrowing；investor learning 与风险溢价（F7、F8 已经排除）；Q-theory 调整成本；Board 的目标函数 |
| 机构改变 power 的转移技术 $T(\cdot)$ | 机构改变 reporting regime 的 law of motion：pending（$\theta$ 不确定）→ resolved（$\theta$ 已知），hazard $h$ |
| 把 off-path 对象放到中心：同组 challenger 替换 incumbent | 把 off-path 对象放到中心：*做真实决策时还不知道它将被如何计量*。在 Stein/Kanodia 类模型里，计量规则固定且是共同知识；pipeline 恰恰是规则存疑的时期 |
| 关键潜变量：$\gamma_A-\gamma_a$ | 关键潜变量：$\sigma_p^2$（结果不确定性）与 $\lambda=\omega b$（reading intensity） |
| 非单调预测：intermediate groups | 非单调预测：contested proposals（$\pi\approx 1/2$） |
| Proxy：jati 人口占比分三档 | Proxy：comment letters 的立场分歧、ED 里的 Alternative Views、tone |
| 第二个 comparative static：$\eta$ | 第二个 comparative static：$\lambda$（transient ownership、face-value reading） |
| 新变量：concentration index $H$ | 新变量：variance-weighted exposure $\sum_p e_{ip}^2\sigma_p^2$ |
| 新检验：RES × H | 新检验：PE 与 $\sum e^2\sigma^2$ 的 horse race；contested bins |

### 3.2 为什么是这两件零件：高管引语本身就在描述它们

| 引语（memo 5–8/18） | 模型成分 |
|---|---|
| Echelon："the biggest question is what is the investor response to these new reported earnings … If they don't, we'll all have to figure out what we're going to do" | $b>0$（数字在 level 上被读）+ 等到读法确定 |
| Cooper Cameron："Until FASB comes out with their guidelines, we're not going to make a decision" | W（推迟） |
| Peet's："I really don't want to come up with a solution while the issues keep changing" | W |
| Senior Housing："transactions being delayed … until they know what the rules are going to be"；更短的 lease term | W + 对规则稳健的交易结构 |
| FedEx："that will depend on how you want to read our balance sheet" | $b$（读法） |
| MicroStrategy："our reported earnings will be far more transparent to investors" | $b$，而且是一个会让投资"读得更好"的规则（$\theta>0$） |
| UNFI："we'd be caught, or stuck, with a higher interest rate" | contracting 子渠道（写在报表数字上的合约） |

这让模型 "economically real"（slides p.47）。T11 可以把这些引语变成数据。

政治经济学的零件（Tullock contest；Crawford–Sobel；Downs → Sutton 1984；Watts & Zimmerman 1978）留给一个可选的 lobbying/comment-letter 扩展（§4.3 的 Corollary），不放进 baseline（slides p.42 的 parsimony）。

---

## 4. Step 3：模型（paper-ready English）

### 4.1 Environment

- A manager chooses investment $I\ge 0$ in a project with net present value $V(I)=\gamma I-I^2/2$, where $\gamma$ is the quality of the firm's investment opportunities (proxied by Tobin's q).
- **Reading.** The rule that will govern the project's accounting moves the amounts that short-horizon readers use (earnings, leverage, book values) by $\theta$ per unit of investment. The short-term price is $P=V(I)+b\,\theta I+\varepsilon$ with $b\ge 0$. $b>0$ means that reported amounts move the short-term price *in levels*, because short-horizon investors anchor on reported amounts (Bushee 2001; Hirshleifer and Teoh 2003) or because contracts and ratings are written on them.
- **Objective.** $(1-\omega)V+\omega P=V(I)+\lambda\,\theta I+\omega\varepsilon$, with **reading intensity** $\lambda\equiv\omega b$.
- **Pipeline.** While a proposal is pending, $\theta$ has mean $\bar\theta$ and variance $\sigma^2$. It resolves with hazard $h$ per quarter, after which $\theta$ is known. Only recognition-and-measurement proposals move $\theta$. Display proposals rearrange amounts a reader can reconstruct; disclosure proposals change information but not amounts.
- **Two ways to hold back.**
  - (R) *Reading risk*: the manager evaluates the reading with mean–variance weight $\rho$. Microfoundations: undiversified managerial wealth; meet-or-beat step payoffs (Skinner and Sloan 2002; Graham, Harvey and Rajgopal 2005); covenant or rating thresholds.
  - (W) *Wait-and-see*: a project can be postponed until the rule resolves, keeping a fraction $\delta_j$ of its value (survival × discounting). $\delta_j$ is heterogeneous across projects.

### 4.2 Benchmark

**Lemma 0.** If $\rho=0$ and projects cannot be postponed, $I=\gamma+\lambda\bar\theta$. The pipeline affects investment only through the expected reading $\bar\theta$ (anticipation). A mean-preserving increase in $\sigma^2$ has no effect, and at resolution investment moves by $\lambda(\theta-\bar\theta)$, which is zero on average. The same holds with a fully rational price that conditions on the anticipated investment: the price then loads on $\theta(I-\hat I)$, and rule risk drops out of the first-order condition at $I=\hat I$.

为什么这条最重要：

1. 它说明 WHY 需要什么：$b>0$ 在 level 上，**并且** $\rho>0$ 或 $\delta>0$。
2. 它给 F2 一个明确的含义：平均 rebound 为正（Resolving +1.518）拒绝了 Lemma 0。唯一的出路是 resolution 系统性地是好消息，而 138/152 个 proposal 被 finalize，这一点并不显然（T2 直接检验）。
3. 它回答研讨会上最可能的问题："为什么理性投资者不直接看穿？"——如果他们看穿，你就不会看到 rebound。

### 4.3 Results

全部在 `model_checks.py` 中验证。带条件的地方都写明了条件；Props 2 和 5 的闭式条件取 $\bar\theta=0$。

**Proposition 1 (pending uncertainty lowers investment).**
- (R) $I_R=\dfrac{\gamma+\lambda\bar\theta}{1+\rho\lambda^2\sigma^2}$, so $\partial I_R/\partial\sigma^2<0$.
- (W) Project $j$ is postponed iff $\delta_j>\delta^*=\dfrac{A^2}{A^2+\lambda^2\sigma^2}$, where $A\equiv\gamma+\lambda\bar\theta$. With $\delta_j\sim U(0,1)$, pending-period investment is $I_W=A^3/(A^2+\lambda^2\sigma^2)$, decreasing in $\sigma^2$.
- Both effects vanish when $\lambda=0$: there is no effect for firms whose reported amounts move no price or contract the manager cares about.

**Proposition 2 (who: reading intensity amplifies).** $\partial^2 I/\partial\sigma^2\partial\lambda<0$ in both variants whenever the distortion is modest (R: $\rho\lambda^2\sigma^2<1$, i.e., investment falls by less than half; W: fewer than half of projects are postponed). Transient owners raise both $\omega$ (Bushee 1998) and $b$ (Bushee 2001); dedicated owners lower them. Hence PE × transient < 0 and PE × dedicated > 0.

**Proposition 3 (what: only proposals that move θ).** R&M proposals put variance on $\theta$; display and disclosure proposals do not. If a pending disclosure proposal raises $b$ (as F10 suggests), it lowers *expensed* investment through the anticipation term ($\partial I/\partial b=-\omega$ when $\theta_0=-1$: R&D, SG&A) but not capex ($\theta_0\approx 0$ for capitalized assets).

**Proposition 4 (when: resolution).** Under (R) and (W), investment recovers at resolution on average; under (R) the recovery is $A\rho\lambda^2\sigma^2/(1+\rho\lambda^2\sigma^2)$. Under Lemma 0 it does not recover. Under (W), postponed projects (mass $\lambda^2\sigma^2/(A^2+\lambda^2\sigma^2)$) are executed at resolution, so investment spikes above baseline; under (R) there is no spike.

**Proposition 5 (opportunity quality separates R from W).** Under (R), $\partial^2 I/\partial\sigma^2\partial\gamma<0$ in levels and $=0$ in logs. Under (W), it is $>0$ in logs, and $>0$ in levels when fewer than a quarter of projects are postponed. Deep-in-the-money projects are not worth delaying.

**Proposition 6 (portfolio).** With independent proposals, firm $i$'s reading variance is $\sum_p e_{ip}^2\sigma_p^2$, where $e_{ip}$ are the proposal-level terms that sum to Pipeline Exposure. For a given PE, concentrated exposure means a larger effect. Linear PE is a proxy for this object.

**Proposition 7 (contestedness).** If proposal $p$ is adopted with probability $\pi_p$ and the status quo stays otherwise, $\sigma_p^2=\pi_p(1-\pi_p)\Delta_p^2$. The effect is inverted-U in $\pi_p$, largest where the Board could go either way.

**Corollary (commenting).** Under (R), the value of removing rule risk is $(A^2/2)\,\rho\lambda^2\sigma^2/(1+\rho\lambda^2\sigma^2)$, which rises with $\lambda$ and $\sigma^2$. Exposed firms with short-horizon owners gain most from engaging the Board, so F11 becomes a prediction and not only a validation.

**Dynamics (the small Markov state, slides p.21).** With a two-state regime (pending/resolved) and hazard $h$, postponing is worth $\tilde\delta_j=\delta_j h/(1-\delta_j(1-h))$ per unit of expected post-resolution value, which increases in $h$. Under (W) the effect is larger when resolution is expected soon; under (R) it is not.

### 4.4 A paragraph for the paper

> To organize these results, I write down a simple model in the spirit of Stein (1989) and Bernanke (1983). A manager who places weight on the short-term price chooses investment while a proposal that would change how that investment is recognized or measured is pending. Because short-horizon investors and contracts read reported amounts, the pending proposal makes the price consequence of investing uncertain. If investors fully saw through reported amounts, or if the manager neither disliked this uncertainty nor could wait it out, the pipeline would affect investment only through the expected content of proposals, and investment would not recover on average when proposals resolve. With either ingredient, investment falls while a proposal is pending and recovers when it resolves. The fall is larger for firms held by short-horizon investors, for proposals whose outcome is more uncertain, and for firms whose exposure is concentrated in few proposals, and it is absent for proposals that change only display or disclosure.

### 4.5 模型刻意不包含的东西

Board 的目标函数与 agenda 选择；投资者的 learning 与风险溢价（F7/F8 已处理）；一般均衡；F10 背后的 reporting-discretion 机制。关于最后一项：Van Landuyt & White (2026) 的逻辑是 preparer 无法把估计量 tailor 到一个未知的规则，所以 bias 更小，ERC 更高。如果想用一个模型同时解释两个应用，可以加一个 reporting-discretion block，让同一个 primitive（"tailoring 需要知道规则"）同时生成 ERC ↑ 和投资的 reading 成本 ↑。但这是更多的机器，只有在它能解释更多时才值得（slides p.42, 45）。

### 4.6 判断：考虑过但不推荐的版本（slides p.47–48）

- **完整的理性 signal-jamming 均衡 + 时机选择。** 这会出现多重均衡，代数很重，而关键洞见已经被 Lemma 0 抓住了。不值得。
- **Ambiguity aversion（maxmin）。** 这是得到 R 的另一种方式：不确定性集合的宽度一阶地压低投资，预测与 R 基本相同。放在脚注里作为 R 的替代 microfoundation 即可。
- **显式的 covenant 模型。** 这是一个子渠道。用 T13 去检验它，而不是去建模它。

---

## 5. Step 4：理论对象 → 数据（slides p.31）

slides p.31 的原话是 "Theory converts an observed demographic variable into a proxy for a latent strategic object"。下表是这篇 paper 的对应版本（✓ = 已有，★ = 新建）。

| 模型对象 | 含义 | Proxy |
|---|---|---|
| $e_{ip}$ | 公司对 proposal $p$ 的 exposure | Eq. (4) 在 proposal 层面的各项 ✓ |
| $\sigma_p^2$ | 结果不确定性 | comment-letter LM uncertainty ✓；反对信的比例（LLM 编码立场）★；ED 里的 "Alternative Views"（发布时的 Board 分歧，事前可观察）★；re-exposure ✓；ED→final 的内容变化（事后，参照 Monsen 2022）★ |
| $\pi_p$ | 通过的概率 | 支持信比例 ★；Big-4 立场（Monsen 2022）★；Board 投票与 dissent ★ |
| $\theta$ 是否变动 | 是否改变投资的计量 | R&M / display / disclosure ✓；与资本投资相关的 topics ★（T4） |
| $\omega$ | 对短期价格的权重 | transient/dedicated ✓；CEO equity vesting（Edmans, Fang & Lewellen 2017）★；即将 SEO ★ |
| $b$ | 报表数字在 level 上被读 | transient ✓；retail/attention ★；公司层面的 ERC ★；covenant 松紧与 frozen/floating GAAP ★ |
| $\rho$ | 短期 payoff 的 concavity | CEO delta（+）与 vega（−），ExecuComp，Core & Guay (2002) ★；接近 meet-or-beat ★ |
| $\delta$ | 可推迟性 | redeployability ✓（Kim & Kung 2017）；product-market fluidity ★（Hoberg, Phillips & Prabhala 2014） |
| $h$ | resolution 的 hazard | board minutes 里的审议阶段 ★（为了确定 timeline 你已经收集了 minutes） |
| 实施 vs resolution | 区分 burden 渠道 | final ASU 的 effective dates ★ |
| $\lambda=0$ 的样本 | 没有短期股价 | 有公开债务但无公开股权的 10-K filers ★ |

---

## 6. Step 5：预测与 prediction matrix（slides p.13–18）

**条件（p.13）**：效应存在，当且仅当 (i) $\lambda=\omega b>0$；(ii) proposal 在投资的计量上放了不确定性（R&M，$\sigma^2>0$）；(iii) $\rho>0$ 或 $\delta>0$。每一条都有数据对应物（§5）。

**Heterogeneity（p.14）**：transient ↑；contested proposals；concentrated exposure；hazard 更高（W）；CEO delta 更高（R）。

**Auxiliary predictions（p.15）**：commenting 随 exposure × transient 上升；letters 表达的关切；disclosure 压低 R&D/SG&A 而不压低 capex；earnings calls 里 "等一等" 的讨论；topic-specific 的真实反应（T15）。

**Prediction matrix**

列：R = reading risk；W = wait-and-see；Antic. = anticipation（只有均值）；RO-CF = 现金流上的 real options；Burden = implementation burden；CoC = cost of capital；Learn = learning from prices；Contract = debt contracting。符号：− 负，+ 正，0 无，✓/✗ = 与该事实相符/不符，? = 模型不给出明确方向。

| # | 预测 | R | W | Antic. | RO-CF | Burden | CoC | Learn | Contract | 状态 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | R&M PE ⇒ I ↓ | − | − | −（若不利） | − | − | − | − | − | 已做（F1, F4） |
| 2 | display/disclosure ⇒ capex 0 | 0 | 0 | 0 | 0 | − | − | ± | 0 | 已做（F4） |
| 3 | uncertainty 胜过 negativity、attention | ✓ | ✓ | ✗ | ✓ | ✗ | ? | ? | ✓ | 已做（F5） |
| 4 | resolution 时平均 rebound | + | + | 0 | + | −（final 之后） | + | + | +（不确定性版本） | 已做（F2） |
| 5 | resolution 后超过 baseline 的 catch-up | 0 | + | 0 | + | 0 | 0 | 0 | 0 | 弱（F9）→ T2 |
| 6 | PE × transient | − | − | 0/− | 0 | 0 | ? | ? | 0 | 已做（F3） |
| 7 | PE × q（levels / logs） | − / 0 | + / + | 0 | + | ? | 0 | − | 0 | +（F8）→ T6 |
| 8 | ICC | 0 | 0 | 0 | 0 | 0 | + | 0 | 0 | 已做（F7） |
| 9 | 价格信息含量 | 0 | 0 | 0 | 0 | 0 | 0 | − | 0 | 已做（F8） |
| 10 | PE × redeployability | 0 | + | 0 | + | 0 | 0 | 0 | 0 | 弱（F9） |
| 11 | $\sum e^2\sigma^2$ 在 PE 之外的解释力 | − | − | 0 | − | 0 | ? | ? | − | 新 T1 |
| 12 | contestedness 的 inverted-U | ✓ | ✓ | ✗（单调于 $\pi$） | ✓ | ✗ | ? | ? | ✓ | 新 T7 |
| 13 | final→effective 窗口内的效应 | 0 | 0 | 0 | 0 | − | 0 | 0 | −（floating GAAP） | 新 T8 |
| 14 | 临近 resolution 时效应更大 | 0 | + | 0 | + | 0 | 0 | 0 | 0 | 新 T9 |
| 15 | CEO delta 放大 / vega 减弱 | ✓ | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 新 T6 |
| 16 | 没有交易股权的公司 | 0 | 0 | ? | − | − | − | 0 | − | 新 T12 |
| 17 | frozen-GAAP covenants 减弱效应 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ✓ | 新 T13 |
| 18 | commenting 随 exposure × transient 上升 | + | + | 0 | 0 | 0 | 0 | 0 | 0 | 新 T10 |
| 19 | disclosure PE ⇒ R&D/SG&A ↓，capex 0 | ✓ | ✓ | ? | 0 | −（两者都降） | ? | ? | 0 | 新 T3 |

**现有证据怎么读**

- #3、#4 拒绝 anticipation；#2、#4 拒绝 burden；#8 拒绝 cost of capital；#7、#9 拒绝 learning；#6 拒绝纯现金流的 real options。
- 剩下的是 reading（R 或 W）和 debt contracting。contracting 与 reading 共享很多预测，但不共享 #6、#16、#18，所以靠 T10/T12/T13 来分。
- 在 reading 内部，#5（catch-up 不稳健）指向 R，#7（PE×q > 0）和 #10（redeployability 为正）指向 W。**这是目前最大的开放问题**，T2 + T6 可以裁决。也可能两者都有：一部分投资可以推迟，一部分不可以。那样模型识别的是两者的混合比例。

---

## 7. Step 6：实证设计与优先级（slides p.16, 18）

每个检验写明：做什么 / 数据 / 预测 / 成本。

### 7.1 Pre-flight（先做，因为模型建立在 F1 之上）

**T14 — 按 lineage 计 exposure；把 re-exposure 当作事件**［现有 register；1–2 天］
- 按 project lineage 重建 register，使每个 lineage 同时最多一个 pending 文件：re-exposure 发布时关闭旧文件，也就是正文自己写的退出规则。然后重估主要结果。
- 把 re-exposure 当作一个信息事件：修改后的 ED 同时改变 $\bar\theta$ 和 $\sigma^2$（例如 2013 年的 lease ED）。

**T5 — Placebos 与 timing permutation**［现有；2–3 天］
- *No requirement changed* 组件应该为 0；目前是 −1.411（t = −4.83）。
- Timing permutation：保留每个 proposal 的 topics 和持续时间，随机重抽 issue date（或整体平移 ±k 个季度），重建 PE，重估 1,000 次，看真实系数落在 placebo 分布的什么位置。这与你的 XBRL permutation 是同一种思路。
- Pre-issue 检验：proposal 发布前 4 个季度的 exposure 应该为 0。*Diverse-practice* proposals 是例外：模型预测它们发布之前投资就被压低（现状本身不确定），发布时反而上升。这把 F6 的 +0.709 从事后解释变成事前预测。

**T4 — 与投资相关的 topics（placebo）**［现有 + topic 分类；2–3 天］
- 事前写好一条规则，把 ASC topics 按"是否决定资本投资的计量"分类，用 LLM 编码加人工核对。相关的例子：360 PP&E、840/842 leases、410 ARO、350 intangibles/goodwill、805 business combinations、835-20 interest capitalization、330 inventory、340-40 contract costs、730 R&D。不相关的例子：260 EPS、205-40 going concern、855 subsequent events、958 not-for-profit。
- 预测：效应集中在相关组件；不相关组件 ≈ 0。
- 专门检查 2008 Going Concern：(a) 它在 margin 分类里属于哪一类；(b) 它的窗口与 2013-013 重叠、被重复计算的部分；(c) 加入 distress 控制之后（Altman Z / O-score；Audit Analytics 的 going-concern 审计意见），它的影响是否还在。Going concern 属于 ASC 205-40，而 ASC 205 的 dictionary 里有 "going concern"、"discontinued operation"（OA2）。如果它映射到 ASC 205，它在 2008–2014 年的影响可能部分来自危机时期的 distress。如果驱动结果的是不相关组件，WHY 的问题就比模型更大。

### 7.2 核心模型检验

**T1 — Quadratic exposure 的 horse race**［现有；2 天］
- 构造 $e_{ipq}=\sum_{o\in O_p}s_{ioq}/|O_p|$（$p\in P_q$），于是 $PE_{iq}=\sum_p e_{ipq}$。
- $PE^{var}_{iq}=\sum_p e_{ipq}^2\,u_p$，其中 $u_p=1$（纯集中度），或 $u_p$ = 标准化后的 letter uncertainty（$\hat\sigma_p^2$）。另加 $HHI_{iq}=\sum_p e_{ipq}^2/PE_{iq}^2$。
- 回归 $I/K_{iq}=\beta_1 PE+\beta_2 PE^{var}+\text{controls}+\alpha_i+\mu_{j(i)q}$。Reading（variance）预测 $\beta_2<0$ 且 $\beta_1$ 收缩；anticipation/burden 预测 $\beta_1<0$、$\beta_2\approx 0$。
- 先做 T14，按 lineage 聚合。
- memo 1(b) 的 IBM/Oracle（PE 几乎一样，共同部分只有一半，最大的组成来自不同 proposal）正好可以示范 Prop 6：算出两家的 HHI，模型说它们的反应应该不同。

**T2 — Resolution event study（分组）**［现有 + outcome 编码；1 周］
- 构造 firm × lineage 面板，event time $\tau$ 相对于 resolution。回归 $I/K_{iq}$ 于 $\sum_p e_{ip}\,\mathbb 1[\tau_{pq}=k]$，$k\in\{\le -5,-4,\dots,+8\}$，含 firm FE 与 FF48×quarter FE。resolution 季度用 day-fraction exposure，避免半个季度的机械效应。
- 分组：(a) final 且变化有限；(b) final 且有实质变化；(c) withdrawn/removed；以及 tone（high uncertainty vs high negativity）。
- 预测：
  - R 和 W：所有 outcome 组在 $\tau=0$ 都跳回，且集中在 high-uncertainty proposals。
  - W：$\tau=0..2$ 出现超过零的 spike，累积 catch-up ≈ 累积缺口 × 存活率。R：没有 spike。
  - Anticipation：只有 (c) 和变软的 (b) 反弹；high-negativity 且被 finalize 的 proposals 不反弹。
  - Burden：finalize 之后下降加深。
- 报告累积和，用 two-way clustering（firm 和 quarter）。memo 的 catch-up 检验在 two-way 下失去显著性，所以先算 MDE。

**T6 — R vs W**［现有 + ExecuComp；3–4 天］
- PE × q 分别用 logs（$\ln(1+I/K)$，或 I/K 除以公司均值）和 levels 估计；PE × redeployability（已有）；PE × CEO delta 与 vega。
- R 的预测：q 在 levels 为负、在 logs 为 0；delta 放大，vega 减弱；redeployability 为 0。
- W 的预测：q 两种都为正；delta/vega 为 0；redeployability 为正。

**T3 — 投资类型**［现有 Compustat；2 天］
- 把 total investment 拆成 capex、R&D、SG&A 组织资本，分别对 R&M/display/disclosure 组件回归。
- 预测：R&M ⇒ capex ↓；disclosure ⇒ R&D/SG&A ↓（通过 $b$），capex 不变。Burden ⇒ 全都 ↓。
- 这是 F10（ERC）和投资之间最直接的联系，也是最推测性的一条。

### 7.3 需要新数据（Phase B）

**T7 — Contestedness 的 inverted-U**［LLM 编码；1–2 周］
- 用你现有的 LLM pipeline 给每封 comment letter 编码立场：support / support with changes / oppose。$\hat\pi_p$ = 支持比例。再从 ED 文本中抽出 Alternative Views（发布时就可观察，是事前变量）。
- 按 $\hat\pi_p(1-\hat\pi_p)$，或按 low/middle/high support 分档构造 PE。
- 预测：中间档（contested）效应最大。anticipation/burden 预测效应单调于 $\pi$。

**T8 — Effective dates**［ASUs；3–4 天］
- 收集每个 final ASU 的 effective date 和 transition method。把 exposure 分成 pending（issue→final）、implementation window（final→effective）、in force 三段。
- Reading 预测只有 pending 有效应；burden 预测 implementation window 有；contracting（floating GAAP）预测 effective date 附近有。

**T9 — 审议阶段 / hazard**［board minutes；1 周］
- 标出 comment deadline、redeliberation 开始、tentative decisions、finalize 投票。
- W 预测晚期阶段（预期等待短）效应更大。但 tentative decisions 也会降低 $\sigma^2$，所以两者都要编码。R 预测平坦。

**T10 — Comment letters 作为 auxiliary 证据**［现有 letters + LLM；1 周］
- Commenting ~ entering exposure × transient share：reading 预测为正。
- 把 letters 表达的关切编码为四类：(a) 用户/投资者会如何读这些数字（波动、"does not reflect the economics"、杠杆观感）；(b) 合约、covenants、ratings；(c) 实施成本；(d) 对最终规则、effective date、transition 的不确定。
- Reading 预测：(a) 在 short-horizon owners 的公司更常见，而且表达 (a) 的公司投资下降更多。

### 7.4 可选（Phase C）

- **T11 — Earnings-call transcripts**（StreetEvents）：构造公司-季度层面关于 pending standards 的讨论，按渠道分类（wait-and-see、reading、financing/covenants、cost），用 memo 里的引语作为 seeds。
- **T12 — $\lambda=0$ 的样本**：有公开债务但无公开股权的 10-K filers。Reading 预测无效应；RO-CF、burden、contracting 预测有效应。比较逻辑同 Asker, Farre-Mensa & Ljungqvist (2015) 对上市与非上市公司投资的比较。
- **T13 — Contracting 子渠道**（Dealscan + credit agreements）：covenant 松紧，以及 credit agreement 里的 GAAP-change 条款（frozen vs floating GAAP；Beatty, Ramesh & Weber 2002），用 LLM 编码。
- **T15 — Topic-specific 的真实反应**：对 topic $o$ 上 pending proposals 的 exposure，应该压低受 topic $o$ 计量的那类投资（leases → 租赁资产；805 → 收购，Compustat AQC；350 → 无形资产），并可能替代到计量已确定的资产上。UNFI（买而不租）和 Senior Housing（更短的 lease term）描述的就是这种替代。注意：对 lease 重的公司，这种替代可能让 capex *上升*，与主结果方向相反；这也是为什么要按投资类型检验。先看 Qiu & Ronen (2025) 在 lease ED 上已经做了什么。

### 7.5 优先级

| Phase | 检验 | 数据 |
|---|---|---|
| A（第 1–3 周） | T14 → T5 → T4 → T1 → T2 → T6（q、redeployability）→ T3 | 全部已有 |
| B（第 4–6 周） | T7、T8、T10、T9、T6（ExecuComp） | LLM 编码 + 少量收集 |
| C（可选） | T11、T12、T13、T15、calibration | 较重 |

---

## 8. 模型强制你做的测量决定

1. **不确定性的单位是 project，不是文件**（T14）。
2. **哪些 proposal 是 placebo**：no requirement changed，以及与投资计量无关的 topics（T4、T5）。它们现在不是零，要先解释。
3. **Exposure 怎么聚合**：线性 PE 是 $\sum e^2\sigma^2$ 的 proxy（Prop 6），两者都报告。
4. **分解的解读**：模型的对象是 within-firm 的 pending/resolved 变化。between-firm 的 disclosure 系数（−7.174）混入了公司类型（比如资产轻的公司），不是模型的对象；paper 里把它和 within 分开讨论。

---

## 9. Step 7：需要多少模型？（slides p.42–45）

- **这篇 paper：applied model，不做 structural estimation。** 模型已经 (i) 解释了机制，(ii) 生成了可区分的预测，(iii) 告诉你要收集什么数据。slides p.42 的建议是："Then perhaps: stop."
- **Structure 能买到什么。** memo 1/18 里 FASB 主席那段引语引出的政策问题是：*审议过程本身的成本*。反事实包括更短的 pendency（更高的 $h$）、公布 tentative decisions（更低的 $\sigma^2$）、re-expose 还是 finalize、捆绑 proposals（集中度）。简约式的 $\beta$ 在这些变化下不是不变的：在 W 下，$h$ 同时改变每季度的反应和持续时间（slides p.43 的逻辑）。
- **推荐的中间方案：一个 calibration box。**
  - 把 Prop 1 和 Prop 4 当作 sufficient statistics，把 $\beta$（每 SD PE）换算成每个 proposal-季度损失的 capex。
  - 计算一个项目的 pendency 带来的投资成本（例如 2010–2016 年的 leases），并展示它在 R 和 W 下如何随 $h$ 变化。
  - 示意：$\omega b=0.15$、$\mathrm{sd}(\theta)=0.3$、$\gamma=0.25$ 时，W 推迟了 3.1% 的 pending 期投资，与 F1 的数量级（3.3%）相当。所以模型不需要极端参数。这只是示意，不是 calibration。
- **如果以后要估计**：用 SMM。Moments = issuance 与 resolution 附近的 event-time profile（下降、rebound、catch-up）、ownership gradient、q gradient；参数 = $\rho\lambda^2\sigma^2$ 和 $\delta$ 的分布。repo 里的 `Notebooks/SMM` 就是现成的工具。这适合放到后续 paper。

---

## 10. Model ownership（slides p.49–50）

| 假设 | 为什么需要 | 依赖它的结果 | 去掉会怎样 | 检验 |
|---|---|---|---|---|
| $b>0$ in levels | 没有它就是 Lemma 0 | Props 1–7 | 只剩 anticipation；没有平均 rebound | F3、T10、T12、T13 |
| $\omega>0$ | manager 在乎短期价格 | 全部 | 会计与决策无关 | F3、T12、CEO vesting |
| $\rho>0$ 或 $\delta>0$ | hold back 的理由 | Props 1, 2, 4, 5 | 回到 Lemma 0 | F2、T2、T6 |
| 只有 R&M 移动 $\theta$ | 定义"pending 的是什么" | Prop 3 | display/disclosure 会有效应（limited-attention 版本） | F4、T3 |
| proposals 相互独立（按 lineage） | 聚合 | Prop 6 | 改用 lineage 层面的协方差 | T14、T1 |
| pipeline 外生于公司 | 公司不能改变 $\sigma^2$ | Props 1–7 | 变成 lobbying 扩展 | T10 |
| 二次的 $V$ | 闭式解 | R 下 Prop 5 在 levels 的符号 | 一般 concave $V$ 下 Props 1, 2, 4 的符号不变；R 下 Prop 5 取决于 $V'''$ | — |

**研讨会问答**（slides p.50）

- *为什么理性投资者不直接看穿？* 他们可能会。那样只有均值重要（Lemma 0），resolution 时不会有平均 rebound。但我们看到了 rebound。ownership gradient 说明起作用的是 short-horizon holders 的价格（Bushee 2001）。
- *这不就是 real options 吗？* 现金流上的 real options 预测没有 ownership gradient（F3），而且没有交易股权的公司也会有效应（T12）。W 确实是一个 real option，但它的标的是 reading，不是现金流。
- *Hold back 是生成的还是假设的？* 是生成的。在 W 中它来自最优化后的目标函数在 $\theta$ 上的凸性（期权价值）；在 R 中它来自 concavity，而 concavity 被挂钩到可观察变量上（delta/vega、benchmarks）。
- *为什么只有 R&M？* Display 可以重构；disclosure 不改变价格所锚定的数字（Prop 3）。
- *会不会是 distress 或危机？* T4/T5 的 placebos；going concern。
- *效应在经济上重要吗？* 见 calibration box。

**LLM 与 attribution**（slides p.46–50）：本文的代数由 `model_checks.py` 验证，但你应该亲手重推 Props 1–5（一共不到一页），直到它成为 "your model"。架构来自 Stein (1989)、Bebchuk & Stole (1993)、Bernanke (1983)；level loading 的动机来自 Bushee (2001)、Hirshleifer & Teoh (2003)；anticipation vs uncertainty 的区分来自 Chang et al. (2023)。本文所有引用在使用前都需要逐条核对。

---

## 11. 写作：模型放在哪里、paper 的架构

- **方案 A**：保留 measurement paper，加一节 §5.1.2 "Why would a pending rule lower investment? A simple model"（正文 2–3 页 + 附录证明）；用 prediction matrix 替换 memo 11/18 的 channel 表；把 T1/T2/T4/T5 作为模型检验报告。
- **方案 B**：拆分。measurement paper 保持精简（测量 + 验证，也许加 ERC）；investment 应用成为一篇围绕模型、带新数据（T7–T13）的机制 paper。
- **建议**：Phase A 之后再决定，这是你和 Laurence 要一起定的。如果 T1/T2 结果干净（quadratic exposure 占优；不依赖方向的 rebound 集中在 uncertain proposals），方案 B 有一个值得单独成文的机制。如果 placebos 不过，先修测量。

---

## 12. 时间表（8 周）

| 周 | 内容 |
|---|---|
| 1 | 写模型节（setup、Lemma 0、Props 1–5）；手推；和 `model_checks.py` 对照 |
| 2 | Pre-flight：T14（lineage）、T5（placebos/permutation）、T4（investment-linked；going concern） |
| 3 | T1（quadratic exposure）、T2（resolution event study）、T6（q 的 logs/levels、redeployability）、T3 |
| 4–5 | LLM 编码：letter 立场（T7）、letter 关切（T10）、Alternative Views；收集 effective dates（T8）和 minutes 里的阶段（T9）；合并 ExecuComp |
| 6 | 运行 T7–T10 和 T6（ExecuComp） |
| 7 | 写作：模型节 + 检验；给 Laurence 的 memo v8（prediction matrix + 结果） |
| 8 | 缓冲；可选 T11–T13、T15、calibration |

---

## 13. 如果预测失败（决策树）

- Placebos 不过（T4/T5）→ 事实还不是事实。先修测量，再建模。
- Rebound 跟着 negativity 而不是 uncertainty，adverse 的 final 之后也没有 rebound → anticipation 渠道。围绕 $\bar\theta$ 重写模型（Lemma 0 的世界）。它仍然是一个模型，只是 WHY 不同。
- 线性 PE 胜过 quadratic，contestedness 是单调的 → anticipation 或 burden。
- 效应出现在 implementation window（final→effective）→ burden。
- 没有交易股权的公司同样有效应，新检验里没有 ownership gradient → 现金流 real options 或 contracting。
- R vs W：出现 catch-up spike 且 q（logs）为正 → W；没有 spike 且 delta 放大 → R；两种迹象都有 → 混合（部分投资可推迟）。

这正是模型有用的地方：它可能失败，而且失败的方式会告诉你下一步做什么（slides p.12, 17–18）。

---

## 14. 需要核对的参考文献

按角色分组。使用前逐条核对年份、期刊和具体结论。

- **架构**：Stein (1989, QJE)；Narayanan (1985, JF)；Bebchuk & Stole (1993, JF)；Kanodia & Sapra (2016, JAR)；Bernanke (1983, QJE)；McDonald & Siegel (1986, QJE)；Bloom (2009, Econometrica)。
- **Policy uncertainty**：Rodrik (1991, JDE)；Julio & Yook (2012, JF)；Pástor & Veronesi (2012, JF)；Gulen & Ion (2016, RFS)；Hassan, Hollander, van Lent & Tahoun (2019, QJE)；Chang, Hajda, Kalmenovitz & Lopez-Lira (2023)；Kalmenovitz (2023, RFS)。
- **Reading 与 horizon**：Bushee (1998, TAR)；Bushee (2001, CAR)；Hirshleifer & Teoh (2003, JAE)；Graham, Harvey & Rajgopal (2005, JAE)；Skinner & Sloan (2002, RAST)；Edmans, Fang & Lewellen (2017, RFS)。
- **检验工具**：Kim & Kung (2017, RFS)；Hoberg, Phillips & Prabhala (2014, JF)；Core & Guay (2002, JAR)；Asker, Farre-Mensa & Ljungqvist (2015, RFS)；Beatty, Ramesh & Weber (2002, JAE)；Monsen (2022, TAR)；Qiu & Ronen (2025, RAST)；Van Landuyt & White (2026, MS)。
- **可选的 lobbying 扩展**：Watts & Zimmerman (1978, TAR)；Sutton (1984, AOS)；Tullock (1980)；Crawford & Sobel (1982, Econometrica)。
- **Slides 里的例子**：Padró i Miquel (2007, ReStud)；Anderson & Francois (2023, JPubE)。
