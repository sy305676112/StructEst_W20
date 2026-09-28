# 为 Pipeline Exposure 的 investment 结果建一个 applied model：计划（v2）

*v2 按你的要求收窄了起点事实：只解释 (A) PE 降低投资，(B) memo v7 里的新结果。paper 里的其他结果不作为起点事实，模型不以它们为目标。*
*依据：Francois, "How to Build a Political Economy Model"（IGC-BREAD Week 3 slides）；memo v7（Sep 24, 2026）；paper draft（Aug 2026）。*
*配套：`model_checks.py` 用 sympy 验证本文所有比较静态、条件和 timing 计算（`python3 model_checks.py`，38/38 通过）。*
*LaTeX 版模型节：`latex/model_section.tex`，证明在 `latex/model_appendix.tex`，单独预览用 `latex/model_standalone.tex`。*
*引用约定：slides p.x = BREAD slide 编号；memo x/18 = memo 页脚编号；Table/OA = paper 编号。offset = Resolving 系数 ÷（−Active 系数），即 resolve 的那部分 exposure 抵消了多少 Active 效应。*

---

## 0. 一页摘要

**起点事实**（§1 详列）

- **A. PE ↑ ⇒ 投资 ↓**（memo 9/18）。
- **B. memo v7 的新结果**
  - B1 timing：pending 时投资下降；resolve 的季度和下一季度恢复；issue 的季度没有额外效应（10/18）。
  - B2 ownership：transient owners 放大，dedicated owners 减弱，按 transient 四分位单调（13–14/18）。
  - B3 cost of capital：ICC 不变（16/18）。
  - B4 learning：nsync 不变；PE×q、PE×return 不为负（17/18）。
  - B5 real options：PE×Redeploy 弱正；catch-up 弱（18/18）。
- 高管引语（5–8/18）只作定性动机。
- 其余结果都不作为起点事实。memo 15/18 的 comment-letter tone 在 paper 里已有（Table 9），我按"其余"处理，只在检验里用作不确定性的 proxy。如果你想把它算进来，模型不用改：Prop 1 本来就预测效应集中在结果不确定的 proposals 上。

**这些事实怎样钉住机制**（§2）

- B2（ownership gradient）⇒ 渠道经过"数字如何被读"，不经过现金流。
- B1（resolve 时恢复，尽管 152 个 proposals 里 138 个最终被 finalize）⇒ 起作用的是不确定性，不是预期内容。
- B3、B4 ⇒ 既不是投资者的折现率，也不是 manager 从价格中学习。
- B4 的 PE×q 和 B5 ⇒ 现有证据偏向"晚投"（W），而不是"少投"（R）。

合起来就是 **reading uncertainty + wait-and-see**。

**一句话 WHY**

> A pending proposal that would change how an investment is recognized or measured makes it uncertain how today's investment will show up in the numbers that short-horizon investors read. A manager who weighs those numbers holds investment back until the reading is known.

**模型骨架**（spare parts，slides p.23, 39–40）：Stein (1989) / Bebchuk–Stole (1993) 的 myopic-manager 架构，加上 Bernanke (1983) 的 wait-and-see。FASB pipeline 改变的是 *reporting regime 的 law of motion*（pending → decided），正如 slides 里 reservation 改变的是 *political power 的 law of motion*（p.26）。

**模型带来了什么**（对照 slides p.35 "What did the modelling actually add?"）

1. **Lemma 0（benchmark）。** 如果价格完全理性、manager 风险中性又不能推迟，那么规则的*不确定性*不影响投资，只有*预期内容*起作用，resolve 时投资平均也不会恢复。B1 拒绝了这个 benchmark。所以 memo 12/18 的 "with the mapping uncertain, holds back" 需要两样东西：数字在 level 上被读，**加上**一个 hold back 的理由——concave 的短期 payoff（R），或推迟的期权（W）。
2. **Timing 命题（Prop 4）。** 它把 memo 10/18 的回归翻译成模型语言。如果不确定性恰好从 ED 发布持续到 ASU 发布，那么 Entering 和 Resolving 在 k=0 都应该约为 Active 效应的一半。memo 的点估计是 0.06 和 0.88。按点估计粗算，不确定性在 ED 发布前约 60 天就已存在，在 ASU 发布前约 46 天基本结束。这与 Board 先在公开会议上做决定、之后才发布文件的程序一致。在 W 下，0.88 超出一半的部分也可以是被推迟投资的 catch-up。
3. **R 与 W 的裁决点在 k=0。** memo 18/18 的 catch-up 从 k=1 开始算。W 预测被推迟的投资在 Board 一做决定就执行，也就是落在 k=0，已经被 Resolving 的 k=0 系数吸收了。
4. **第二个 comparative static 和一个形状预测。** reading intensity $\lambda=\omega b$；不确定性渠道下效应按 $\lambda^2$ 放大，anticipation 下按 $\lambda$ 放大；若 $\lambda$ 与 transient 持股成正比，前者对持股是二次的，后者是线性的。
5. **两个新变量/新预测。** $\sum_p e_{ip}^2\sigma_p^2$（slides 里 concentration index $H$ 的对应物）；contestedness 的 inverted-U（"contesting jatis" 的对应物）。

**我的建议**：以 W（"wait until the reading is known"）为主版本，R 作为 robustness variant。第一优先是 timing 检验 T1：按 Board 的决定日重新定日期，看 k=0 是否仍有超出半季度基准的恢复。

**测量检查**（这些不是新事实，而是起点事实本身）：Table OA1 显示，同一项目的原 ED 和 re-exposure 常常同时算作 pending（leases、revenue、going concern、income-tax disclosure 等）。这直接影响 Active/Entering/Resolving 的定义，所以 T1 之前要先按 project lineage 重建（M1）。

**第一步**（Phase A，约 3 周，现有数据 + board minutes）：M1 lineage → T1 timing → T3 R vs W → T2 不确定性 vs 预期内容 → T4 quadratic exposure → M2/M3 validity。

---

## 1. 起点事实（Step 1，slides p.11）

### A. PE ↑ ⇒ 投资 ↓（memo 9/18）

| | (1) I/K | (2) I/K | (3) I/K | (4) Total inv. |
|---|---|---|---|---|
| PE | −2.283*** | −1.509*** | −1.531*** | −1.080*** |
| Controls | No | No | Yes | Yes |
| FE | firm + quarter | firm + FF48×quarter | firm + FF48×quarter | firm + FF48×quarter |

×1,000 per SD of PE；col (3) 约为均值的 3%。paper 的 Table 8 是较早版本（−2.620、−1.765、−1.683、−1.094），写作时统一用一个版本。

### B. memo v7 的新结果

**B1 Timing（10/18）**：$I/K_{q+k}$ 对 $Active_q$、$Resolving_q$、$Entering_q$ 回归。Active = q 中 pending（= PE）；Resolving = q 中被 finalize 或 withdraw；Entering = q 中发布。

| | k = 0 | k = 1 | k = 2 |
|---|---|---|---|
| Active | −1.725*** | −1.546*** | −1.381*** |
| Resolving | +1.518*** | +1.385** | +0.738 |
| Entering | +0.101 | +0.318 | +0.584 |
| offset（Resolving ÷ −Active） | 0.88 | 0.90 | 0.53（n.s.） |
| Entering ÷ −Active | 0.06 | 0.21 | 0.42（均 n.s.） |

**B2 Ownership（13–14/18）**
- PE × z(transient)：−1.012***（I/K），−0.670***（total）。
- PE × z(dedicated)：+0.609***，+0.416***。
- 按 transient 四分位的 PE 斜率：−0.79、−1.05、−2.16、−3.15（Q4 = Q1：p < 0.0001）。

**B3 Cost of capital（16/18）**
- ICC 对 PE：四个模型都不显著，composite −1.05bp（t = −0.40），MDE 约 7–10bp。
- 控制 ICC 后，PE 对 I/K 的系数不变（−1.454 → −1.454）。

**B4 Learning（17/18）**
- nsync 对 PE：0.0004（t = 0.10）。
- PE × q：+0.581（t = 1.44，I/K），+0.651**（t = 2.12，total）。
- PE × past 12-month return：+0.155（t = 0.69）。

**B5 Real options（18/18）**
- PE × Redeploy：+0.413*（t = 1.70）；去掉 oil & gas 为 +0.310（t = 1.11）。
- Finalize 之后的 catch-up，$\sum_{k=1}^{4}$：I/K 0.098，total 2.462**（two-way t = 1.12）；$\sum_{k=1}^{8}$：I/K 1.375，total 5.530***（two-way t = 1.43）。

**定性动机**：高管引语（5–8/18），见 §3.2。

**不作为起点事实**：paper 里按 margin 和按理由的分解；comment-letter attention/tone（包括 memo 15/18）；ERC；commenting；Apple/TI 与 IBM/Oracle 例子（后者在 T4 里只用作示范）。

---

## 2. 这些事实怎样钉住机制

| 起点事实 | 排除 | 指向 |
|---|---|---|
| B2 ownership gradient | 现金流上的 real options；implementation burden；经由现金流的 anticipation | 渠道经过"数字如何被读"（$\lambda$） |
| B1 resolve 时恢复（k=0、1 的 offset 约 0.9） | anticipation（Lemma 0）；burden（它预测 finalize 后效应持续或加深） | 起作用的是不确定性（$\sigma^2$） |
| B1 Entering ≈ 0 | — | 不确定性在 ED 发布之前就已存在（Prop 4） |
| B3 ICC 不变 | cost of capital | — |
| B4 nsync 不变、PE×return ≈ 0 | learning from prices | — |
| B4 PE×q ≥ 0（levels） | learning；R（R 预测为负） | W |
| B5 PE×Redeploy > 0（弱） | anticipation 与 R（两者都预测约为 0） | W |
| B5 k ≥ 1 没有 catch-up | catch-up 逐渐发生的 W | R，或 catch-up 发生在 k=0 的 W |

两点说明：

- anticipation 也能产生 ownership gradient（如果预期内容通过 reading 起作用，效应按 $\lambda\bar\theta$ 放大）。所以区分 anticipation 与不确定性的是 B1，而不是 B2；B2 区分的是 reading 与现金流渠道。两者合起来才是 "reading uncertainty"。
- B3 和 B4 里的 nsync 不是模型"解释"出来的，而是模型不放投资者风险溢价和 learning 这两块机器的理由（slides p.23 "discard irrelevant machinery"）。

---

## 3. Step 2：借机制、拆零件（slides p.23–24, 36, 39–41）

### 3.1 slides 的例子和这篇 paper 一一对应

| Anderson–Francois (2023) | 这篇 paper |
|---|---|
| 母模型：Politics of Fear（Padró i Miquel 2007） | 母模型：Stein (1989) / Bebchuk–Stole (1993) myopia + Bernanke (1983) wait-and-see |
| 保留：group control 的价值 + incumbent 保住控制权的优势 | 保留：manager 对短期价格的权重 $\omega$ + 报表数字进入短期价格 |
| 丢弃：taxation、specialization、patronage | 丢弃：Stein 的 signal-jamming 不动点和 earnings borrowing；投资者 learning 与风险溢价（B3、B4 已排除）；Q-theory 调整成本；Board 的目标函数 |
| 机构改变 power 的转移技术 $T(\cdot)$ | 机构改变 reporting regime 的 law of motion：pending（$\theta$ 不确定）→ decided（$\theta$ 已知），hazard $h$ |
| 把 off-path 对象放到中心：同组 challenger 替换 incumbent | 把 off-path 对象放到中心：*做真实决策时还不知道它将被如何计量*。在 Stein/Kanodia 类模型里，计量规则固定且是共同知识；pipeline 恰恰是规则存疑的时期 |
| 关键潜变量：$\gamma_A-\gamma_a$ | 关键潜变量：$\sigma_p^2$（结果不确定性）与 $\lambda=\omega b$（reading intensity） |
| 非单调预测：intermediate groups | 非单调预测：contested proposals（$\pi\approx 1/2$） |
| Proxy：jati 人口占比分三档 | Proxy：comment letters 的立场分歧；ED 里的 Alternative Views |
| 第二个 comparative static：$\eta$ | 第二个 comparative static：$\lambda$（short-horizon ownership） |
| 新变量：concentration index $H$ | 新变量：variance-weighted exposure $\sum_p e_{ip}^2\sigma_p^2$ |
| 新检验：RES × H | 新检验：PE 与 $\sum e^2\sigma^2$ 的 horse race；contested bins |

### 3.2 高管引语本身就在描述这两件零件（memo 5–8/18）

| 引语 | 模型成分 |
|---|---|
| Echelon："the biggest question is what is the investor response to these new reported earnings … If they don't, we'll all have to figure out what we're going to do" | $b>0$（数字在 level 上被读）+ 等到读法确定 |
| Cooper Cameron："Until FASB comes out with their guidelines, we're not going to make a decision" | W（推迟） |
| Peet's："I really don't want to come up with a solution while the issues keep changing" | W |
| Senior Housing："transactions being delayed … until they know what the rules are going to be"；更短的 lease term | W + 对规则稳健的交易结构 |
| FedEx："that will depend on how you want to read our balance sheet" | $b$（读法） |
| MicroStrategy："our reported earnings will be far more transparent to investors" | $b$，而且这个规则会让投资"读得更好"（$\theta>0$） |
| UNFI："we'd be caught, or stuck, with a higher interest rate" | contracting 子渠道（写在报表数字上的合约） |

这让模型 "economically real"（slides p.47）。7 段引语里有 4 段是在说"等"，这也是把 W 作为主版本的理由之一。政治经济学的零件（Tullock contest；Crawford–Sobel；Downs → Sutton 1984；Watts & Zimmerman 1978）只留给一个可选的 lobbying 扩展（§4.3 Corollary），不放进 baseline（slides p.42）。

---

## 4. Step 3：模型（paper-ready English）

### 4.1 Environment

- A manager chooses investment $I\ge 0$ in a project with net present value $V(I)=\gamma I-I^2/2$, where $\gamma$ is the quality of the firm's investment opportunities (proxied by Tobin's q).
- **Reading.** The rule that will govern the project's accounting moves the amounts that short-horizon investors use (earnings, leverage, book values) by $\theta$ per unit of investment. The short-term price is $P=V(I)+b\,\theta I+\varepsilon$ with $b\ge 0$. $b>0$ means that reported amounts move the short-term price *in levels*, because short-horizon investors anchor on reported amounts (Bushee 2001; Hirshleifer and Teoh 2003).
- **Objective.** $(1-\omega)V+\omega P=V(I)+\lambda\,\theta I+\omega\varepsilon$, with **reading intensity** $\lambda\equiv\omega b$.
- **Pipeline.** A proposal puts uncertainty on $\theta$ if it would change how the investment is recognized or measured. While the rule is effectively pending, $\theta$ has mean $\bar\theta$ and variance $\sigma^2$. The Board decides with hazard $h$ per quarter, after which $\theta$ is known. Effective dates need not coincide with document dates: the Board deliberates and votes in public meetings before it publishes an exposure draft or a final Update.
- **Two ways to hold back.**
  - (R) *Reading risk*: the manager evaluates the reading with mean–variance weight $\rho$ (undiversified wealth; meet-or-beat payoffs, Graham, Harvey and Rajgopal 2005).
  - (W) *Wait-and-see*: a project can be postponed until the Board decides, keeping a fraction $\delta_j$ of its value (survival × discounting), heterogeneous across projects. Investment made now can be adjusted after the decision at cost $\tfrac{k}{2}(\Delta I)^2$; $k$ measures irreversibility.

### 4.2 Benchmark

**Lemma 0.** If $\rho=0$ and projects cannot be postponed, $I=\gamma+\lambda\bar\theta$. The pipeline affects investment only through the expected reading $\bar\theta$ (anticipation). A mean-preserving increase in $\sigma^2$ has no effect, and when the Board decides, investment moves by $\lambda(\theta-\bar\theta)$, which is zero on average. The same holds with a fully rational price that conditions on the anticipated investment: the price then loads on $\theta(I-\hat I)$, and rule risk drops out of the first-order condition at $I=\hat I$.

为什么这条最重要：

1. 它说明 WHY 需要什么：$b>0$ 在 level 上，**并且** $\rho>0$ 或 $\delta>0$。
2. 它给 B1 一个明确含义：offset 约 0.9 拒绝了 Lemma 0。唯一的出路是 Board 的决定系统性地是好消息，而 152 个 proposals 里 138 个被 finalize，这一点并不显然（T2 直接检验）。
3. 它回答研讨会上最可能的问题："为什么理性投资者不直接看穿？"——如果他们看穿，就不会有 B1 的恢复。

### 4.3 Results

以下每条都在 `model_checks.py` 里验证过。Props 2 和 5 中关于 $\lambda$、$\gamma$ 的闭式条件取 $\bar\theta=0$。

**Proposition 1 (pending uncertainty lowers investment).**
- (R) $I_R=\dfrac{\gamma+\lambda\bar\theta}{1+\rho\lambda^2\sigma^2}$, decreasing in $\sigma^2$.
- (W) Project $j$ is postponed iff $\delta_j>\delta^*=\dfrac{A^2}{A^2+\lambda^2\sigma^2}$, where $A\equiv\gamma+\lambda\bar\theta$. With $\delta_j\sim U(0,1)$, pending-period investment is $I_W=A^3/(A^2+\lambda^2\sigma^2)$, decreasing in $\sigma^2$.
- Both effects vanish when $\lambda=0$.

**Proposition 2 (who: reading intensity).** For small $\sigma^2$ the pending-period cut scales with $\lambda^2$: about $A\rho\lambda^2\sigma^2$ under (R) and $\lambda^2\sigma^2/A$ under (W). The cut steepens in $\lambda$ whenever the distortion is modest (R: $\rho\lambda^2\sigma^2<1$; W: fewer than half of projects postponed). Transient owners raise $\omega$ (Bushee 1998) and $b$ (Bushee 2001); dedicated owners lower them. Hence PE × transient < 0 and PE × dedicated > 0, and, if $\lambda$ is proportional to the transient share, the decline is quadratic in that share under both variants and linear under anticipation.

**Proposition 3 (the Board decides).** Once $\theta$ is known, new investment returns to $\gamma+\lambda\theta$. On average this is a recovery under (R) and (W), and none under Lemma 0. Under (W), the postponed projects (mass $\lambda^2\sigma^2/(A^2+\lambda^2\sigma^2)$) are executed at once, so the decision quarter contains a catch-up; under (R) it does not.

**Proposition 4 (timing in the Active/Entering/Resolving regression).** Let a pending proposal lower quarterly investment in proportion to the share of the quarter during which its rule is effectively pending, with document dates uniform within quarters.
1. If the rule is effectively pending exactly between the exposure draft and the final Update, the Entering and Resolving coefficients at $k=0$ both equal about half of $|\beta|$ (the Active effect), and the Resolving coefficient at $k\ge 1$ equals the full Active effect.
2. If the effective start precedes the exposure draft by a share $a$ of a quarter and the effective decision precedes the Update by a share $c$, the $k=0$ coefficients are $|\beta|(1-a)^2/2$ for Entering and $|\beta|\,[1-(1-c)^2/2]$ for Resolving.
3. Under (W), the Resolving coefficient at $k=0$ also contains the catch-up of postponed projects.

读 memo 10/18：Entering ÷ −Active = 0.06，offset = 0.88。在 (R) 下，这意味着 $a\approx 0.66$（约 60 天）、$c\approx 0.51$（约 46 天）。Entering 很不精确（t = 0.19），所以 $a$ 只是粗略的。在 (W) 下，0.88 中超出一半的部分也可以是 catch-up，那样 $c$ 会更小。k=1 的 offset（0.90）接近完全抵消，与模型一致；k=2 的 0.53 不精确。k=1、2 的 Entering 点估计为正（+0.32、+0.58，均不显著），与 W 的 hazard 逻辑一致：新发布的 proposal 预期等待时间长，被推迟的投资少。

**Proposition 5 (how the manager holds back: R vs W).**
- *Opportunity quality.* (R): $\partial^2 I/\partial\sigma^2\partial\gamma<0$ in levels and $=0$ in logs. (W): $>0$ in logs, and $>0$ in levels when fewer than a quarter of projects are postponed. Deep-in-the-money projects are not worth delaying.
- *Irreversibility.* (W): the postponed share $\lambda^2\sigma^2 k/[(1+k)(A^2+\lambda^2\sigma^2)]$ rises with $k$, so PE × redeployability > 0. (R): the pending-period cut is $A\rho\lambda^2\sigma^2$ to first order for every $k$ (with symmetric $\theta$), so PE × redeployability ≈ 0. Under Lemma 0, initial investment is $A$ for every $k$, so the interaction is 0.
- *Catch-up.* Yes under (W), at the decision; no under (R).

**Proposition 6 (portfolio).** With independent proposals, firm $i$'s reading variance is $\sum_p e_{ip}^2\sigma_p^2$, where $e_{ip}$ are the proposal-level terms that sum to PE. For a given PE, concentrated exposure means a larger effect; linear PE is a proxy for this object.

**Proposition 7 (contestedness).** If proposal $p$ is adopted with probability $\pi_p$ and the status quo stays otherwise, $\sigma_p^2=\pi_p(1-\pi_p)\Delta_p^2$. The effect is inverted-U in $\pi_p$, largest where the Board could go either way.

**Corollary (commenting; optional).** Under (R), the value of removing rule risk is $(A^2/2)\,\rho\lambda^2\sigma^2/(1+\rho\lambda^2\sigma^2)$, which rises with $\lambda$ and $\sigma^2$. Exposed firms with short-horizon owners gain most from engaging the Board.

**Dynamics (the small Markov state, slides p.21).** With two states (pending/decided) and hazard $h$, postponing is worth $\tilde\delta_j=\delta_j h/(1-\delta_j(1-h))$ per unit of expected post-decision value, which increases in $h$. Under (W) the effect is larger when a decision is expected soon; under (R) it is not.

### 4.4 Scorecard：起点事实 × 模型

✓ = 相符，✗ = 不符，"（弱）" = 对应的证据本身较弱。

| 起点事实 | Lemma 0 | R | W | 命题 |
|---|---|---|---|---|
| A：PE ↓ 投资 | ✓（若 $\bar\theta$ 不利） | ✓ | ✓ | Prop 1 |
| B1：Board 决定后恢复 | ✗ | ✓ | ✓ | Prop 3 |
| B1：Entering ≈ 0，k=0 的 offset 0.88 | ✗（预测不恢复） | ✓（有效日期早于文件日期） | ✓（同左，或 k=0 的 catch-up） | Prop 4 |
| B2：PE×transient < 0，PE×dedicated > 0 | ✓（若经由 reading） | ✓ | ✓ | Prop 2 |
| B3：ICC 不变 | ✓ | ✓ | ✓ | 设计选择：模型里没有投资者折现率 |
| B4：nsync 不变，PE×return ≈ 0 | ✓ | ✓ | ✓ | 设计选择：模型里没有 learning |
| B4：PE×q ≥ 0（levels） | ✓（预测 0） | ✗（预测为负） | ✓ | Prop 5 |
| B5：PE×Redeploy > 0 | ✗（弱；预测 0） | ✗（弱；预测约 0） | ✓ | Prop 5 |
| B5：k ≥ 1 没有 catch-up | ✓ | ✓ | ✓（若 catch-up 在 k=0）；✗（若逐渐发生） | Props 3–4 |

结论：Lemma 0 不符合 B1；R 不符合 B4 的 q 和 B5 的 redeployability；只要 catch-up 发生在 k=0，W 与所有起点事实相符。所以 T1 是关键检验。

### 4.5 A paragraph for the paper

> To organize these results, I write down a simple model in the spirit of Stein (1989) and Bernanke (1983). A manager who places weight on the short-term price chooses investment while a proposal that would change how that investment is recognized or measured is pending. Because short-horizon investors read reported amounts, the pending proposal makes the price consequence of investing uncertain. If investors saw through reported amounts, or if the manager could neither wait nor disliked the uncertainty, the pipeline would affect investment only through the expected content of proposals, and investment would not recover on average once the Board decides. With either ingredient, investment falls while a proposal is pending and recovers when the Board decides. The fall is larger for firms held by short-horizon investors. When the manager can wait, it is smaller for firms with better investment opportunities and more redeployable assets, and postponed investment is made as soon as the Board decides.

### 4.6 模型刻意不包含的东西，以及考虑过的替代版本

**不包含**：
- Board 的目标函数与 agenda 选择；一般均衡。
- 投资者的 learning 与风险溢价（B3、B4）。
- paper 的其他结果：按 margin/理由的分解、ERC、commenting。它们不是起点事实，模型不以它们为目标。

**考虑过、但不推荐的版本**（slides p.47–48）：
- *完整的理性 signal-jamming 均衡 + 时机选择*：会出现多重均衡，代数很重，而关键洞见已经被 Lemma 0 抓住了。
- *Ambiguity aversion（maxmin）*：是得到 R 的另一种方式，预测与 R 基本相同，放在脚注里作为替代 microfoundation 即可。
- *显式的 covenant 模型*：它是一个子渠道，用 T9 去检验，而不是去建模。

---

## 5. Step 4：理论对象 → 数据（slides p.31）

slides 原话："Theory converts an observed demographic variable into a proxy for a latent strategic object"。（✓ = 已有，★ = 新建）

| 模型对象 | 含义 | Proxy |
|---|---|---|
| $e_{ip}$ | 公司对 proposal $p$ 的 exposure | Eq. (4) 在 proposal 层面的各项 ✓ |
| 有效起点 | 规则"进入议程" | 加入 technical agenda 的日期；Board 投票发布 ED 的会议 ★（board minutes，你已收集） |
| 有效决定 | 规则"已定" | Board 确认决定或投票 finalize 的会议 ★（同上） |
| $\sigma_p^2$ | 结果不确定性 | comment-letter LM uncertainty ✓（仅作 proxy）；反对信比例（LLM 编码立场）★；ED 里的 Alternative Views ★；re-exposure ✓ |
| $\pi_p$ | 通过的概率 | 支持信比例 ★；Big-4 立场（Monsen 2022）★；Board 投票与 dissent ★ |
| $\theta$ 是否变动 | 是否改变投资的计量 | 与资本投资相关的 ASC topics ★（M3） |
| $\omega$ | 对短期价格的权重 | transient/dedicated ✓；CEO equity vesting（Edmans, Fang & Lewellen 2017）★ |
| $b$ | 报表数字在 level 上被读 | transient ✓；retail 持股、analyst coverage ★ |
| $\rho$ | 短期 payoff 的 concavity | CEO delta（+）与 vega（−），ExecuComp，Core & Guay (2002) ★ |
| $k$、$\delta$ | 不可逆性、可推迟性 | redeployability ✓（Kim & Kung 2017）；product-market fluidity ★（Hoberg, Phillips & Prabhala 2014） |
| $h$ | Board 做决定的 hazard | board minutes 里的审议阶段 ★ |
| 实施期 | 区分 burden | final ASU 的 effective dates ★ |
| $\lambda=0$ 的样本 | 没有短期股价 | 有公开债务但无公开股权的 10-K filers ★ |

---

## 6. Step 5：新预测与 prediction matrix（slides p.13–18）

**条件（p.13）**：效应存在，当且仅当 (i) $\lambda=\omega b>0$；(ii) proposal 在投资的计量上放了不确定性；(iii) $\rho>0$ 或 $\delta>0$。

**Prediction matrix。** 只列新检验，不列起点事实（后者见 §4.4）。cost of capital 和 learning 已被 B3/B4 排除，不再列。

列：R = reading risk；W = wait-and-see；Antic. = anticipation（只有均值）；RO-CF = 现金流上的 real options；Burden = implementation burden；Contract = debt contracting。

| # | 预测 | R | W | Antic. | RO-CF | Burden | Contract | 检验 |
|---|---|---|---|---|---|---|---|---|
| 1 | 按 Board 决定日重新定日期后，k=0 仍超出半季度基准 | 0 | + | 0 | + | − | 0 | T1 |
| 2 | 恢复与决定的方向无关（按原案 finalize / 修改后 finalize / withdraw） | ✓ | ✓ | ✗（只有利好才恢复） | ✓ | ✗ | ✓ | T2 |
| 3 | ownership gradient 是二次的（PE × M²；若 λ 与 M 成正比） | ✓ | ✓ | ✗（线性） | 0 | 0 | 0 | T2 |
| 4 | PE × q 用 logs | 0 | + | 0 | + | ? | 0 | T3 |
| 5 | CEO delta 放大，vega 减弱 | ✓ | 0 | 0 | 0 | 0 | 0 | T3 |
| 6 | $\sum e^2\sigma^2$ 在 PE 之外的解释力 | − | − | 0 | − | 0 | − | T4 |
| 7 | contestedness 的 inverted-U | ✓ | ✓ | ✗（单调于 $\pi$） | ✓ | ✗ | ✓ | T5 |
| 8 | final → effective 窗口内的效应 | 0 | 0 | 0 | 0 | − | −（floating GAAP） | T6 |
| 9 | 临近决定时效应更大（hazard） | 0 | + | 0 | + | 0 | 0 | T7 |
| 10 | 没有交易股权的公司 | 0 | 0 | 0 | − | − | − | T8 |
| 11 | frozen-GAAP covenants 减弱效应 | 0 | 0 | 0 | 0 | 0 | ✓ | T9 |
| 12 | commenting 随 exposure × transient 上升 | + | + | 0 | 0 | 0 | 0 | T10 |

**还开着的问题**：R vs W（#1、#4、#5、#9）；不确定性 vs 预期内容的稳健性（#2、#3）；reading vs contracting（#10、#11）。

模型还预测效应集中在改变投资计量的 proposals、以及结果不确定的 proposals。paper 里有相关结果，但按你的要求它们不是起点事实；以后需要时可以作为 out-of-sample 检验。

---

## 7. Step 6：实证设计与优先级（slides p.16, 18）

### 7.1 测量检查（起点事实本身）

**M1 — 按 lineage 定义 Active/Entering/Resolving**［现有 register；1–2 天；T1 的前提］
- 按 Table OA1，以下文件都与自己的 re-exposure 同时算作 pending：leases 2010-010 与 2013-012；revenue 2010-006 与 2011-011；going concern 2008-019 与 2013-013；income-tax disclosure 2016-010、2019-005 与 2023-001；loss contingencies 2008-010 与 2010-009；transfers 2005-020 与 2008-013（后者标题即 "Revision of 8/11/05 ED"）；debt classification 2017-001 与 2019-015。正文的退出规则是 "a re-exposure that supersedes it" 结束窗口，Table 1 却只记了 2 个 superseded（都是 EPS）。
- 模型里不确定性的单位是*最终会生效的那条规则*，所以：
  - Active 按 lineage 只计一次；
  - Resolving = lineage 被 finalize 或 withdraw；
  - Entering = 新 lineage 的第一份 ED；
  - re-exposure 是 lineage 内部的事件，单独设一个变量，既不算 Resolving 也不算 Entering。
- 然后重估 A 和 B1。

**M2 — Timing permutation**［现有；2 天］
- 保留每个 proposal 的 topics 和持续时间，随机重抽 issue date，重建 PE，重估 1,000 次，看真实系数落在 placebo 分布的什么位置。这和你的 XBRL permutation 是同一思路。
- 顺带：paper 里 no-requirement-changed 那一格 within-firm 是 −1.411（t = −4.83），按模型应为 0，permutation 可以说明这类窗口效应有多常见。

**M3 — 与投资计量相关的 topics**［现有 + topic 分类；2–3 天］
- 事前写好规则，把 ASC topics 按"是否决定资本投资的计量"分类（LLM 编码 + 人工核对）。相关的例子：360、840/842、410、350、805、835-20、330、340-40、730。不相关的例子：260、205-40、855、958。
- 预测：效应集中在相关 topics。
- 专门看一下 2008 Going Concern（去掉它 A 的系数缩小 38.6%，OA6）：它的窗口有一部分与 2013-013 重复计算；加入 distress 控制（Altman Z / O-score；Audit Analytics 的 going-concern 意见）后，它的影响是否还在。

### 7.2 核心检验（Phase A）

**T1 — Timing：把 B1 变成对模型的检验**［现有 + board minutes；1–2 周；第一优先］

(a) **半季度基准。** 用 day-fraction 计 Active（一个季度中 pending 的天数占比），保留 Entering/Resolving。如果文件日期就是有效日期，且在 R 下，Entering/Resolving 的系数应为 0。按 memo 的点估计，Entering 会为负（issue 的季度效应已经是"满"的）、Resolving 为正（恢复早于文件日期）。

(b) **按 Board 事件重新定日期。** 用 LLM 从 minutes 中抽取：
- 项目加入 technical agenda 的日期；
- Board 投票发布 ED 的会议；
- Board 确认决定或投票 finalize 的会议。

用这些日期重算 day-fraction exposure。预测：
- R：Entering 和 Resolving 都约为 0；
- W：在 Board 决定的季度出现超出基准的正向 spike（catch-up），之后约为 0。

(c) **从 k=0 开始算 catch-up。** 以 (b) 的决定日为 event time 0，把决定季度及之后的累积 I/K 与 pending 期的累积缺口对比。W 预测大部分缺口在 k=0–1 被补回，R 预测不补回。用 two-way clustering（firm 和 quarter），先算 MDE。memo 18/18 的检验从 k=1 开始，恰好漏掉了 W 预测 catch-up 发生的季度。

(d) **Placebo。** 项目加入议程之前的 exposure 应为 0；议程到 ED 之间的 exposure 应为负（B1 的 Entering ≈ 0 说明不确定性那时已经存在）。

**T2 — 不确定性 vs 预期内容**［现有 + outcome 编码；1 周］

(a) **按决定的方向分组。** 分为按原案 finalize、修改后 finalize（修改方向：对投资的报告更有利或更不利）、withdraw 三组。不确定性渠道预测三组都恢复；anticipation 预测只有利好的决定才恢复。

(b) **Ownership gradient 的形状。** 回归中加入 PE × M 和 PE × M²（或更细的分组）。若 $\lambda$ 与 M 成正比，不确定性渠道预测二次（按 $\lambda^2$），anticipation 预测线性（按 $\lambda$）。memo 的四分位点估计还判断不了形状：Q3→Q4 的斜率反而比 Q2→Q3 平。

**T3 — R vs W**［现有 + ExecuComp；3–4 天］
- 用 logs（$\ln(1+I/K)$，或 I/K 除以公司均值）重估 B4 的 PE × q 和 B5 的 PE × redeployability：R 预测都约为 0，W 预测都为正。
- 加入 PE × CEO delta 与 vega：R 预测 delta 放大、vega 减弱；W 预测都约为 0。

**T4 — Quadratic exposure 的 horse race**［现有；2 天］
- 构造 $e_{ipq}=\sum_{o\in O_p}s_{ioq}/|O_p|$，并在 M1 之后按 lineage 聚合；$PE^{var}_{iq}=\sum_p e_{ipq}^2 u_p$，其中 $u_p=1$，或 $u_p$ = 标准化后的 letter uncertainty（仅作 $\hat\sigma_p^2$ 的 proxy）。另加 $HHI_{iq}=\sum_p e_{ipq}^2/PE_{iq}^2$。
- 回归 $I/K=\beta_1 PE+\beta_2 PE^{var}+\dots$。预测：$\beta_2<0$，且 $\beta_1$ 收缩。
- memo 1(b) 的 IBM/Oracle（PE 几乎相同，共同部分只有一半）可以用来示范 Prop 6。

### 7.3 需要新数据（Phase B）

- **T5 — Contestedness 的 inverted-U**［LLM 编码；1–2 周］：给每封 comment letter 编码立场（support / support with changes / oppose），并从 ED 文本中抽出 Alternative Views（事前可观察）。按 $\hat\pi_p(1-\hat\pi_p)$ 或 low/middle/high support 分档构造 PE。预测中间档效应最大。
- **T6 — Effective dates**［ASUs；3–4 天］：把 exposure 分成 pending、implementation window（final → effective）和 in force 三段。只有 burden 和 floating-GAAP contracting 预测 implementation window 有效应。
- **T7 — 审议阶段与 hazard**［与 T1 共用 minutes］：W 预测临近决定的阶段效应更大。由于 tentative decisions 同时会降低 $\sigma^2$，两者都要编码。

### 7.4 可选（Phase C）

- **T8 — $\lambda=0$ 的样本**：有公开债务但无公开股权的 10-K filers。reading 渠道预测无效应（逻辑同 Asker, Farre-Mensa & Ljungqvist 2015）。
- **T9 — Contracting 子渠道**：Dealscan 的 covenants，加上 credit agreements 里的 GAAP-change 条款（frozen vs floating；Beatty, Ramesh & Weber 2002），用 LLM 编码。
- **T10 — Comment letters**：commenting 是否随 exposure × transient 上升；letters 表达的关切是"用户会如何读这些数字"、合约、成本，还是"最终规则不确定"。
- **T11 — Earnings calls**（StreetEvents）：构造公司-季度层面的 "pending standard" 讨论，并按渠道分类，用 memo 的引语作 seeds。
- **T12 — Topic-specific 的真实反应**：leases → 租赁资产，805 → 收购，等等，以及向计量已确定的资产的替代（UNFI、Senior Housing）。先看 Qiu & Ronen (2025) 在 lease ED 上已经做了什么。

### 7.5 优先级

| Phase | 内容 | 数据 |
|---|---|---|
| A（第 1–3 周） | M1 → T1 → T3 → T2 → T4 → M2、M3 | 现有 + board minutes |
| B（第 4–6 周） | T5、T6、T7 | LLM 编码 + 少量收集 |
| C（可选） | T8–T12、calibration | 较重 |

---

## 8. Step 7：需要多少模型？（slides p.42–45）

- **这篇 paper：applied model，不做 structural estimation。** 模型已经 (i) 解释了起点事实，(ii) 生成了可区分的预测，(iii) 告诉你要收集什么数据（minutes 里的决定日、letter 立场、effective dates）。slides p.42："Then perhaps: stop."
- **Structure 能买到什么。** memo 1/18 里 FASB 主席的引语引出的政策问题是*审议过程本身的成本*：更短的审议（更高的 $h$）、更早公布 tentative decisions（更低的 $\sigma^2$）会怎样。简约式的 $\beta$ 在这些变化下不是不变的：在 W 下，$h$ 同时改变每季度的反应和持续时间（slides p.43）。
- **中间方案：一个 calibration box。**
  - 用 Props 1 和 3 把 $\beta$ 换算成每个 proposal-季度损失的 capex，并区分"推迟"（W 下会补回）和"损失"（衰减的部分）。
  - 示意：$\omega b=0.15$、$\mathrm{sd}(\theta)=0.3$、$\gamma=0.25$ 时，W 推迟了 3.1% 的 pending 期投资，与 A 的数量级相当，所以模型不需要极端参数。这只是示意，不是 calibration。
- **以后如果要估计**：用 SMM，moments = Board 事件前后的 event-time profile（T1）、ownership gradient（B2、T2）和 q gradient（T3）。repo 里的 `Notebooks/SMM` 就是工具。适合放到后续 paper。

---

## 9. Model ownership（slides p.49–50）

| 假设 | 为什么需要 | 依赖它的结果 | 去掉会怎样 | 检验 |
|---|---|---|---|---|
| $b>0$ in levels | 没有它就是 Lemma 0 | Props 1–7 | 只剩 anticipation；B1 无法解释 | B2、T8 |
| $\omega>0$ | manager 在乎短期价格 | 全部 | 会计与决策无关 | B2、T8 |
| $\rho>0$ 或 $\delta>0$ | hold back 的理由 | Props 1–5 | 回到 Lemma 0 | B1、T1、T3 |
| 有效日期早于文件日期 | 让 Prop 4 与 B1 的 k=0 系数吻合 | Prop 4 | 预测 Entering 和 Resolving 都约为半个 Active | T1(b) |
| 只有改变投资计量的 proposal 才移动 $\theta$ | 定义"pending 的是什么" | Prop 1 的范围 | 所有 topics 都有效应 | M3 |
| proposals 相互独立（按 lineage） | 聚合 | Prop 6 | 改用 lineage 层面的协方差 | M1、T4 |
| pipeline 外生于公司 | 公司不能改变 $\sigma^2$ | 全部 | 变成 lobbying 扩展 | T10 |
| 二次的 $V$ | 闭式解 | R 下 Prop 5 在 levels 的符号 | 一般 concave $V$ 下 Props 1–3 的符号不变 | — |

**研讨会问答**（slides p.50）
- *为什么理性投资者不直接看穿？* 他们可能会；那样只有均值重要（Lemma 0），B1 的恢复就不会出现。ownership gradient 说明起作用的是 short-horizon holders 的价格。
- *这不就是 real options 吗？* 现金流上的 real options 预测没有 ownership gradient（B2）。W 确实是一个 real option，但标的是 reading，不是现金流。
- *Hold back 是生成的还是假设的？* 在 W 中，它来自最优化后的目标函数在 $\theta$ 上的凸性（期权价值），是生成的；在 R 中，它来自 concavity，而 concavity 挂钩到 CEO delta/vega。
- *为什么 issue 的季度没有额外效应，resolve 的季度又恢复得这么快？* 因为 Board 在公开会议上先定、后发布（Prop 4）；T1(b) 直接检验。
- *会不会是 distress 或危机？* 见 M2、M3。
- *效应在经济上重要吗？* 见 calibration box。

**LLM 与 attribution**（slides p.46–50）：代数由 `model_checks.py` 验证，但你应该亲手重推 Lemma 0 和 Props 1–5（一共不到两页），直到它成为 "your model"。架构来自 Stein (1989)、Bebchuk & Stole (1993)、Bernanke (1983)；level loading 的动机来自 Bushee (2001)、Hirshleifer & Teoh (2003)；anticipation vs uncertainty 的区分来自 Chang et al. (2023)。所有引用在使用前都需要逐条核对。

---

## 10. 写作：模型放在哪里

- 起点事实都在 investment 上，所以模型节属于 investment 应用。
- **方案 A**：保留 measurement paper，加一节 "Why would a pending rule lower investment? A simple model"（正文 2–3 页 + 附录证明），用 §4.4 的 scorecard 替换 memo 11/18 的 channel 表，把 T1–T4 作为模型检验。paper 里的分解和 ERC 保留为描述性结果，不由模型解释。
- **方案 B**：把 investment 应用拆成一篇围绕模型、带新数据（minutes、letter 立场、effective dates）的机制 paper。
- **建议**：Phase A 之后再决定，这需要你和 Laurence 一起定。如果 T1 干净（按 Board 决定日重新定日期后，k=0 的恢复和 catch-up 清楚可见），方案 B 有一个值得单独成文的机制。

---

## 11. 时间表（8 周）

| 周 | 内容 |
|---|---|
| 1 | 写模型节（Lemma 0、Props 1–5），手推；M1 lineage |
| 2 | T1(a) 半季度基准；开始从 minutes 抽取 Board 事件日期；M2、M3 |
| 3 | T1(b)–(d) 重新定日期、从 k=0 算 catch-up、placebo；T3；T2(b)；T4 |
| 4–5 | T2(a) 决定方向编码；T5 letter 立场与 Alternative Views；T6 effective dates；T7 阶段；合并 ExecuComp |
| 6 | 运行 T5–T7 |
| 7 | 写作：模型节 + 检验；给 Laurence 的 memo v8（scorecard + T1 结果） |
| 8 | 缓冲；可选 T8–T12、calibration |

---

## 12. 如果预测失败（决策树）

- M1–M3 改变了 A 或 B1 → 先重新确立起点事实。
- T1：重新定日期后 k=0 有超出基准的 spike，且 T3 在 logs 下 q 为正 → W。没有 spike，logs 下 q ≈ 0，且 delta 放大 → R。两种迹象都有 → 混合（部分投资可以推迟）。
- T2：只有利好的决定才恢复，且 ownership gradient 线性 → anticipation。这时围绕 $\bar\theta$ 重写模型（Lemma 0 的世界）。它仍然是一个模型，只是 WHY 变成"预期内容如何被读"。
- T6：效应出现在 implementation window → burden。
- T8：没有交易股权的公司效应一样大 → 现金流渠道或 contracting。

这正是模型有用的地方：它可能失败，而失败的方式会告诉你下一步做什么（slides p.12, 17–18）。

---

## 13. 需要核对的参考文献

按角色分组。使用前逐条核对年份、期刊和具体结论。

- **架构**：Stein (1989, QJE)；Narayanan (1985, JF)；Bebchuk & Stole (1993, JF)；Kanodia & Sapra (2016, JAR)；Bernanke (1983, QJE)；McDonald & Siegel (1986, QJE)；Dixit & Pindyck (1994)；Bloom (2009, Econometrica)。
- **Policy uncertainty**：Rodrik (1991, JDE)；Julio & Yook (2012, JF)；Pástor & Veronesi (2012, JF)；Gulen & Ion (2016, RFS)；Hassan, Hollander, van Lent & Tahoun (2019, QJE)；Chang, Hajda, Kalmenovitz & Lopez-Lira (2023)；Kalmenovitz (2023, RFS)。
- **Reading 与 horizon**：Bushee (1998, TAR)；Bushee (2001, CAR)；Hirshleifer & Teoh (2003, JAE)；Graham, Harvey & Rajgopal (2005, JAE)；Edmans, Fang & Lewellen (2017, RFS)。
- **检验工具**：Kim & Kung (2017, RFS)；Hoberg, Phillips & Prabhala (2014, JF)；Core & Guay (2002, JAR)；Asker, Farre-Mensa & Ljungqvist (2015, RFS)；Beatty, Ramesh & Weber (2002, JAE)；Monsen (2022, TAR)；Qiu & Ronen (2025, RAST)。
- **可选的 lobbying 扩展**：Watts & Zimmerman (1978, TAR)；Sutton (1984, AOS)；Tullock (1980)；Crawford & Sobel (1982, Econometrica)。
- **Slides 里的例子**：Padró i Miquel (2007, ReStud)；Anderson & Francois (2023, JPubE)。

---

## 附：v2 相对 v1 的改动

- 起点事实收窄为 A + memo 新结果；删去为分解、ERC、commenting 设计的部分（v1 的 Prop 3 与投资类型检验）。
- 新增 Prop 4（timing），把 memo 10/18 翻译成对有效日期和 catch-up 的检验；T1 成为第一优先。
- 更正 v1 的 pre-issue placebo：B1 的 Entering ≈ 0 说明议程到 ED 之间不是 placebo，真正的 placebo 是加入议程之前。
- 验证了 redeployability 能区分 W 与 R：R 即使允许事后调整，pending 期的削减在一阶上也与可逆性无关（`model_checks.py` R6、R7）。
- 新增形状预测：不确定性渠道下 ownership gradient 是凸的，anticipation 下是线性的。
- 检验重新编号（M1–M3、T1–T12）。
