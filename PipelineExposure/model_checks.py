"""Symbolic checks for the pending-rule investment model in applied_model_plan.md.

Each check states a claim from the plan and verifies its sign or closed form with
sympy. Run: python3 model_checks.py

Notation (see Section 4 of the plan):
    gamma   investment opportunity (NPV slope; Tobin's q proxy), V(I) = gamma*I - I**2/2
    lam     reading intensity, lam = omega * b
            omega = weight on the short-term price, b = how much the short-term
            price (or a contract) moves with the reported consequence of investment
    thbar   mean of the reading theta while the rule is pending
    s2      variance of theta while the rule is pending (outcome uncertainty)
    rho     concavity of the manager's short-term payoff (variant R)
    delta   survival-and-discount factor of postponing a project (variant W)
"""
import sympy as sp

g, lam, thbar, s2, rho, I, Ihat, h, e1, e2, v1, v2, p, D = sp.symbols(
    "gamma lam thbar s2 rho I Ihat h e1 e2 v1 v2 p Delta", real=True
)

results = []


def check(label, claim, ok, detail=""):
    results.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {label}: {claim}")
    if detail:
        print(f"         {detail}")


A = g + lam * thbar  # investment when the rule is known to be theta = thbar

# ---------------------------------------------------------------- Lemma 0
# Benchmark: risk-neutral manager, no postponement -> I = argmax V(I) + lam*thbar*I
I0 = sp.solve(sp.diff(g * I - I**2 / 2 + lam * thbar * I, I), I)[0]
check("L0a", "benchmark investment = gamma + lam*thbar, independent of s2",
      sp.simplify(I0 - A) == 0 and sp.diff(I0, s2) == 0, f"I0 = {I0}")

# Rational signal-jamming: price loads on theta*(I - Ihat); mean-variance manager.
# FOC evaluated at the equilibrium I = Ihat does not contain s2.
beta, omega = sp.symbols("beta omega", positive=True)
U_rat = (g * I - I**2 / 2 + omega * beta * thbar * (I - Ihat)
         - rho / 2 * omega**2 * beta**2 * s2 * (I - Ihat) ** 2)
foc_eq = sp.diff(U_rat, I).subs(I, Ihat)
check("L0b", "with a fully rational price, rule risk drops out of the FOC at I = Ihat",
      sp.diff(foc_eq, s2) == 0, f"FOC at equilibrium: {sp.simplify(foc_eq)} = 0")

# Resolution under the benchmark: theta = thbar + z with E[z] = 0; I_after is linear in z,
# so its expectation is I_after evaluated at z = 0.
z = sp.Symbol("z", real=True)
I_after = g + lam * (thbar + z)
check("L0c", "benchmark: average change in investment at resolution is zero",
      sp.diff(I_after, z, 2) == 0 and sp.simplify(I_after.subs(z, 0) - I0) == 0,
      "I_after(theta) - I0 = lam*(theta - thbar), mean zero by iterated expectations")

# ---------------------------------------------------------------- Variant R
U_R = g * I - I**2 / 2 + lam * thbar * I - rho / 2 * lam**2 * s2 * I**2
IR = sp.solve(sp.diff(U_R, I), I)[0]
check("R0", "I_R = (gamma + lam*thbar) / (1 + rho*lam^2*s2)",
      sp.simplify(IR - A / (1 + rho * lam**2 * s2)) == 0, f"I_R = {sp.simplify(IR)}")

dIR = sp.simplify(sp.diff(IR, s2))
check("R1", "dI_R/ds2 = -A*rho*lam^2/(1+rho*lam^2*s2)^2  (< 0 iff A>0, rho>0, lam!=0)",
      sp.simplify(dIR + A * rho * lam**2 / (1 + rho * lam**2 * s2) ** 2) == 0)

IR0 = IR.subs(thbar, 0)
cross_lam = sp.factor(sp.diff(IR0, s2, lam))
target = -2 * g * rho * lam * (1 - rho * lam**2 * s2) / (1 + rho * lam**2 * s2) ** 3
check("R2", "thbar=0: d2I_R/ds2 dlam = -2*gamma*rho*lam*(1-rho*lam^2*s2)/(1+rho*lam^2*s2)^3",
      sp.simplify(cross_lam - target) == 0,
      "negative iff rho*lam^2*s2 < 1, i.e. the distortion is below half of investment")

cross_g = sp.simplify(sp.diff(IR, s2, g))
check("R3", "levels: d2I_R/ds2 dgamma = -rho*lam^2/(1+rho*lam^2*s2)^2 < 0  (PE x q NEGATIVE)",
      sp.simplify(cross_g + rho * lam**2 / (1 + rho * lam**2 * s2) ** 2) == 0)

cross_g_log = sp.simplify(sp.diff(sp.log(IR), s2, g))
check("R4", "logs: d2 ln I_R/ds2 dgamma = 0  (PE x q zero in semi-elasticities)",
      cross_g_log == 0)

reb_R = sp.simplify(A - IR)
check("R5", "average rebound at resolution = A*rho*lam^2*s2/(1+rho*lam^2*s2) > 0",
      sp.simplify(reb_R - A * rho * lam**2 * s2 / (1 + rho * lam**2 * s2)) == 0,
      "no catch-up spike: after resolution I = gamma + lam*theta, nothing was postponed")

# ---------------------------------------------------------------- Variant W
# Project-level choice (rho = 0): invest now -> A^2/2 ; wait -> delta*(A^2 + lam^2*s2)/2.
# Postpone iff delta > delta_star = A^2/(A^2 + lam^2*s2).  delta ~ U(0,1) across projects:
# investment while pending = A * delta_star ; mass postponed = 1 - delta_star.
dstar = A**2 / (A**2 + lam**2 * s2)
IW = A * dstar
check("W0", "postponement threshold delta* = A^2/(A^2+lam^2 s2); I_W = A^3/(A^2+lam^2 s2)",
      sp.simplify(IW - A**3 / (A**2 + lam**2 * s2)) == 0)

dIW = sp.simplify(sp.diff(IW, s2))
check("W1", "dI_W/ds2 = -A^3 lam^2/(A^2+lam^2 s2)^2 < 0",
      sp.simplify(dIW + A**3 * lam**2 / (A**2 + lam**2 * s2) ** 2) == 0)

IW0 = IW.subs(thbar, 0)
cW_lam = sp.factor(sp.diff(IW0, s2, lam))
tW_lam = -2 * g**3 * lam * (g**2 - lam**2 * s2) / (g**2 + lam**2 * s2) ** 3
check("W2", "thbar=0: d2I_W/ds2 dlam = -2 gamma^3 lam (gamma^2 - lam^2 s2)/(gamma^2+lam^2 s2)^3",
      sp.simplify(cW_lam - tW_lam) == 0,
      "negative iff gamma^2 > lam^2 s2, i.e. fewer than half of projects are postponed")

cW_g = sp.factor(sp.diff(IW0, s2, g))
tW_g = -g**2 * lam**2 * (3 * lam**2 * s2 - g**2) / (g**2 + lam**2 * s2) ** 3
check("W3", "thbar=0: d2I_W/ds2 dgamma = gamma^2 lam^2 (gamma^2 - 3 lam^2 s2)/(...)^3  (PE x q POSITIVE)",
      sp.simplify(cW_g - tW_g) == 0,
      "positive iff gamma^2 > 3 lam^2 s2 (fewer than a quarter of projects postponed)")

cW_g_log = sp.simplify(sp.diff(sp.log(IW0), s2, g))
check("W4", "logs: d2 ln I_W/ds2 dgamma = 2 gamma lam^2/(gamma^2+lam^2 s2)^2 > 0",
      sp.simplify(cW_g_log - 2 * g * lam**2 / (g**2 + lam**2 * s2) ** 2) == 0)

check("W5", "catch-up at resolution: postponed mass 1 - delta* = lam^2 s2/(A^2+lam^2 s2) invests",
      sp.simplify((1 - dstar) - lam**2 * s2 / (A**2 + lam**2 * s2)) == 0,
      "variant W predicts a spike above baseline at resolution; variant R does not")

# Dynamic version: rule resolves with hazard h; a project survives-and-is-discounted by
# d per quarter. Waiting until resolution is worth d*h/(1-d*(1-h)) per unit of E[Pi(theta)].
d = sp.symbols("d", positive=True)
d_eff = d * h / (1 - d * (1 - h))
check("W6", "effective delta rises with the resolution hazard h (d in (0,1))",
      sp.simplify(sp.diff(d_eff, h) - d * (1 - d) / (1 - d * (1 - h)) ** 2) == 0,
      "so under W the pending effect is larger when resolution is expected soon")

# ---------------------------------------------------------------- Aggregation
from sympy.stats import Normal, variance

ep1, ep2, vp1, vp2 = sp.symbols("e1 e2 v1 v2", positive=True)
X1, X2 = Normal("X1", 0, sp.sqrt(vp1)), Normal("X2", 0, sp.sqrt(vp2))  # independent shocks
var_i = e1**2 * v1 + e2**2 * v2
var_calc = sp.simplify(variance(ep1 * X1 + ep2 * X2))
check("A1", "firm reading variance = sum_p e_ip^2 sigma_p^2 (independent proposals)",
      sp.simplify(var_calc - (ep1**2 * vp1 + ep2**2 * vp2)) == 0,
      "for fixed PE = e1 + e2 it is largest when exposure is concentrated")
PE = sp.symbols("PE", positive=True)
v_conc = sp.simplify(var_i.subs({e2: PE - e1, v1: 1, v2: 1}))
check("A2", "equal sigma: variance minimised at e1 = e2 = PE/2 for given PE",
      sp.solve(sp.diff(v_conc, e1), e1)[0] == PE / 2)

# ---------------------------------------------------------------- Contestedness
s2_bin = p * (1 - p) * D**2
check("C1", "binary outcome: sigma^2 = pi(1-pi) Delta^2, maximised at pi = 1/2 (inverted U)",
      sp.solve(sp.diff(s2_bin, p), p)[0] == sp.Rational(1, 2))

# ---------------------------------------------------------------- Lobbying value
gain_R = sp.simplify(A**2 / 2 - U_R.subs(I, IR))
check("B1", "value of removing rule risk (variant R) = (A^2/2) rho lam^2 s2/(1+rho lam^2 s2)",
      sp.simplify(gain_R - A**2 / 2 * rho * lam**2 * s2 / (1 + rho * lam**2 * s2)) == 0,
      "increasing in lam and s2: exposed firms with short-horizon owners gain most from commenting")

# ---------------------------------------------------------------- Expensed investment
th0, b, om = sp.symbols("theta0 b omega", real=True)
I_exp = g + om * b * th0
check("E1", "expensed investment (theta0 = -1): dI/db = -omega < 0",
      sp.diff(I_exp, b).subs(th0, -1) == -om,
      "a pending rule that raises the ERC (b) lowers R&D/SG&A investment, not capex (theta0 ~ 0)")

# ---------------------------------------------------------------- Illustration
num = {g: sp.Rational(1, 4), lam: sp.Rational(3, 20), s2: sp.Rational(9, 100)}
drop_W = float(1 - dstar.subs(thbar, 0).subs(num))
print(f"\nIllustration (not a calibration): omega*b = 0.15, sd(theta) = 0.3, gamma = 0.25 "
      f"-> variant W postpones {drop_W:.1%} of pending-period investment")

print(f"\n{sum(results)}/{len(results)} checks pass")
