"""Symbolic checks for the pending-rule investment model in applied_model_plan.md (v2).

Each check states a claim from the plan and verifies its sign, closed form or number
with sympy. Run: python3 model_checks.py

Notation (see Section 4 of the plan):
    gamma   investment opportunity (NPV slope; Tobin's q proxy), V(I) = gamma*I - I**2/2
    lam     reading intensity, lam = omega * b
            omega = weight on the short-term price, b = how much the short-term
            price moves with the reported consequence of investment
    thbar   mean of the reading theta while the rule is pending
    s2      variance of theta while the rule is pending (outcome uncertainty)
    rho     concavity of the manager's short-term payoff (variant R)
    delta   survival-and-discount factor of postponing a project (variant W)
    k       cost of adjusting investment after the rule is decided (irreversibility)
"""
import sympy as sp

g, lam, thbar, s2, rho, I, Ihat, h, e1, e2, v1, v2, p, D = sp.symbols(
    "gamma lam thbar s2 rho I Ihat h e1 e2 v1 v2 p Delta", real=True
)

results = []


def check(label, claim, ok, detail=""):
    results.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}: {claim}")
    if detail:
        print(f"         {detail}")


def expect(expr, z, var, m4=None):
    """E[expr] for a polynomial in z with E[z]=0, E[z^2]=var, E[z^3]=0, E[z^4]=m4."""
    poly = sp.Poly(sp.expand(expr), z)
    moments = {0: 1, 1: 0, 2: var, 3: 0, 4: m4}
    return sp.expand(sum(c * moments[m[0]] for m, c in zip(poly.monoms(), poly.coeffs())))


A = g + lam * thbar  # investment when the rule is known to be theta = thbar

# ---------------------------------------------------------------- Lemma 0 (benchmark)
I0 = sp.solve(sp.diff(g * I - I**2 / 2 + lam * thbar * I, I), I)[0]
check("L0a", "benchmark investment = gamma + lam*thbar, independent of s2",
      sp.simplify(I0 - A) == 0 and sp.diff(I0, s2) == 0, f"I0 = {I0}")

# Rational signal-jamming: price loads on theta*(I - Ihat); mean-variance manager.
beta, omega = sp.symbols("beta omega", positive=True)
U_rat = (g * I - I**2 / 2 + omega * beta * thbar * (I - Ihat)
         - rho / 2 * omega**2 * beta**2 * s2 * (I - Ihat) ** 2)
foc_eq = sp.diff(U_rat, I).subs(I, Ihat)
check("L0b", "fully rational price: rule risk drops out of the FOC at I = Ihat",
      sp.diff(foc_eq, s2) == 0, f"FOC at equilibrium: {sp.simplify(foc_eq)} = 0")

z = sp.Symbol("z", real=True)  # theta = thbar + z, E[z] = 0
I_after = g + lam * (thbar + z)
check("L0c", "benchmark: average change in investment at resolution is zero",
      sp.simplify(expect(I_after, z, s2) - I0) == 0,
      "I_after(theta) - I0 = lam*(theta - thbar), mean zero by iterated expectations")

# ---------------------------------------------------------------- Variant R (reading risk)
U_R = g * I - I**2 / 2 + lam * thbar * I - rho / 2 * lam**2 * s2 * I**2
IR = sp.solve(sp.diff(U_R, I), I)[0]
check("R0", "I_R = (gamma + lam*thbar) / (1 + rho*lam^2*s2)",
      sp.simplify(IR - A / (1 + rho * lam**2 * s2)) == 0)
check("R1", "dI_R/ds2 = -A*rho*lam^2/(1+rho*lam^2*s2)^2  (< 0 iff A > 0, rho > 0, lam != 0)",
      sp.simplify(sp.diff(IR, s2) + A * rho * lam**2 / (1 + rho * lam**2 * s2) ** 2) == 0)

IR0 = IR.subs(thbar, 0)
target = -2 * g * rho * lam * (1 - rho * lam**2 * s2) / (1 + rho * lam**2 * s2) ** 3
check("R2", "thbar=0: d2I_R/ds2 dlam = -2 gamma rho lam (1 - rho lam^2 s2)/(1 + rho lam^2 s2)^3",
      sp.simplify(sp.diff(IR0, s2, lam) - target) == 0,
      "negative iff rho*lam^2*s2 < 1, i.e. the distortion is below half of investment")
check("R3", "levels: d2I_R/ds2 dgamma = -rho lam^2/(1 + rho lam^2 s2)^2 < 0  (PE x q NEGATIVE)",
      sp.simplify(sp.diff(IR, s2, g) + rho * lam**2 / (1 + rho * lam**2 * s2) ** 2) == 0)
check("R4", "logs: d2 ln I_R/ds2 dgamma = 0  (PE x q zero in semi-elasticities)",
      sp.simplify(sp.diff(sp.log(IR), s2, g)) == 0)
check("R5", "average recovery at resolution = A rho lam^2 s2/(1 + rho lam^2 s2) > 0, no spike",
      sp.simplify((A - IR) - A * rho * lam**2 * s2 / (1 + rho * lam**2 * s2)) == 0)

# R with ex-post adjustment: invest I0 while pending; once theta is known, move to I1 at
# cost (k/2)(I1 - I0)^2. Symmetric theta. Measured pending-period investment is I0.
k, I0s_, m4 = sp.symbols("k I0 m4", positive=True)
u = A + lam * z
I1 = (u + k * I0s_) / (1 + k)
payoff = u * I1 - I1**2 / 2 - k / 2 * (I1 - I0s_) ** 2
E_pay = expect(payoff, z, s2, m4)
Var_pay = sp.expand(expect(payoff**2, z, s2, m4) - E_pay**2)
I0_R = sp.solve(sp.diff(E_pay - rho / 2 * Var_pay, I0s_), I0s_)[0]
x = rho * lam**2 * s2
cut_R = sp.simplify(A - I0_R)
check("R6", "R with adjustment: pending cut = A x (1+k)/(1+k(1+x)), x = rho lam^2 s2",
      sp.simplify(cut_R - A * x * (1 + k) / (1 + k * (1 + x))) == 0,
      "first order in s2 the cut is A*rho*lam^2*s2 for every k -> PE x redeployability ~ 0 under R")
check("R7", "R: d(cut)/dk = -A x^2/(1+k(1+x))^2 (second order, slightly negative)",
      sp.simplify(sp.diff(cut_R, k) + A * x**2 / (1 + k * (1 + x)) ** 2) == 0)

# ---------------------------------------------------------------- Variant W (wait-and-see)
# Invest now -> A^2/2 ; wait -> delta*(A^2 + lam^2 s2)/2. Postpone iff delta > delta*.
# delta ~ U(0,1) across projects: pending-period investment = A * delta*.
dstar = A**2 / (A**2 + lam**2 * s2)
IW = A * dstar
check("W0", "postponement threshold delta* = A^2/(A^2+lam^2 s2); I_W = A^3/(A^2+lam^2 s2)",
      sp.simplify(IW - A**3 / (A**2 + lam**2 * s2)) == 0)
check("W1", "dI_W/ds2 = -A^3 lam^2/(A^2+lam^2 s2)^2 < 0",
      sp.simplify(sp.diff(IW, s2) + A**3 * lam**2 / (A**2 + lam**2 * s2) ** 2) == 0)

IW0 = IW.subs(thbar, 0)
tW_lam = -2 * g**3 * lam * (g**2 - lam**2 * s2) / (g**2 + lam**2 * s2) ** 3
check("W2", "thbar=0: d2I_W/ds2 dlam = -2 gamma^3 lam (gamma^2 - lam^2 s2)/(gamma^2+lam^2 s2)^3",
      sp.simplify(sp.diff(IW0, s2, lam) - tW_lam) == 0,
      "negative iff fewer than half of projects are postponed")
tW_g = -g**2 * lam**2 * (3 * lam**2 * s2 - g**2) / (g**2 + lam**2 * s2) ** 3
check("W3", "thbar=0: d2I_W/ds2 dgamma > 0 iff gamma^2 > 3 lam^2 s2  (PE x q POSITIVE in levels)",
      sp.simplify(sp.diff(IW0, s2, g) - tW_g) == 0,
      "i.e. whenever fewer than a quarter of projects are postponed")
check("W4", "logs: d2 ln I_W/ds2 dgamma = 2 gamma lam^2/(gamma^2+lam^2 s2)^2 > 0",
      sp.simplify(sp.diff(sp.log(IW0), s2, g) - 2 * g * lam**2 / (g**2 + lam**2 * s2) ** 2) == 0)
check("W5", "catch-up at resolution: postponed mass lam^2 s2/(A^2+lam^2 s2) invests at once",
      sp.simplify((1 - dstar) - lam**2 * s2 / (A**2 + lam**2 * s2)) == 0)

d = sp.symbols("d", positive=True)
d_eff = d * h / (1 - d * (1 - h))
check("W6", "value of waiting d*h/(1-d(1-h)) rises with the resolution hazard h",
      sp.simplify(sp.diff(d_eff, h) - d * (1 - d) / (1 - d * (1 - h)) ** 2) == 0,
      "under W the effect is larger when resolution is expected soon")

# Irreversibility in W: investing now keeps the option to adjust at cost k after the rule
# is decided. Value of investing now = max_I0 E[payoff] (risk neutral).
I0_W = sp.solve(sp.diff(E_pay, I0s_), I0s_)[0]
V_now = sp.simplify(E_pay.subs(I0s_, I0_W))
check("W7a", "risk-neutral initial investment is A for every k (anticipation: redeployability 0)",
      sp.simplify(I0_W - A) == 0)
check("W7b", "value of investing now = (A^2 + lam^2 s2/(1+k))/2",
      sp.simplify(V_now - (A**2 + lam**2 * s2 / (1 + k)) / 2) == 0)
post_share = sp.simplify(1 - V_now / ((A**2 + lam**2 * s2) / 2))
check("W7c", "postponed share = lam^2 s2 k/((1+k)(A^2+lam^2 s2)), increasing in k",
      sp.simplify(post_share - lam**2 * s2 * k / ((1 + k) * (A**2 + lam**2 * s2))) == 0
      and sp.simplify(sp.diff(post_share, k) - lam**2 * s2 / ((1 + k) ** 2 * (A**2 + lam**2 * s2))) == 0,
      "less redeployable (higher k) -> more postponement -> PE x redeployability > 0 under W")

# ---------------------------------------------------------------- Ownership gradient
M, w0, w1, b0, b1 = sp.symbols("M w0 w1 b0 b1", positive=True)
cut_R_small = sp.limit((A - IR) / s2, s2, 0)
cut_W_small = sp.limit((A - IW) / s2, s2, 0)
check("O1", "small s2: cut scales with lam^2 in both variants (R: A rho lam^2, W: lam^2/A)",
      sp.simplify(cut_R_small - A * rho * lam**2) == 0 and sp.simplify(cut_W_small - lam**2 / A) == 0)
lam_M = (w0 + w1 * M) * (b0 + b1 * M)  # omega and b both rise with the transient share M
check("O2", "if omega and b rise with transient share M, lam(M)^2 is convex in M",
      sp.expand(sp.diff(lam_M**2, M, 2)).is_positive is True,
      "so the PE slope should steepen more than linearly across transient-share bins")

# ---------------------------------------------------------------- Timing (memo 10/18)
# Effect in a quarter is proportional to the share of the quarter the rule is effectively
# pending (variant R). Document dates are uniform within the quarter (u ~ U(0,1)).
uu, a, c = sp.symbols("u a c", positive=True)
E_fR = sp.integrate(uu - c, (uu, c, 1))       # effectively pending share, resolution quarter
E_fI = 1 - sp.integrate(uu - a, (uu, a, 1))   # effectively pending share, issue quarter
check("TM1", "resolution quarter: Resolving/|Active| = 1 - (1-c)^2/2  (= 1/2 if c = 0)",
      sp.simplify(E_fR - (1 - c) ** 2 / 2) == 0,
      "c = how far (share of a quarter) the effective decision precedes the published ASU")
check("TM2", "issue quarter: Entering/|Active| = (1-a)^2/2  (= 1/2 if a = 0)",
      sp.simplify((1 - E_fI) - (1 - a) ** 2 / 2) == 0,
      "a = how far (share of a quarter) the effective start precedes the published ED")
r_ent, r_res = sp.Rational(101, 1725), sp.Rational(1518, 1725)  # memo 10/18, k = 0
a_hat = [s for s in sp.solve(sp.Eq((1 - a) ** 2 / 2, r_ent), a) if 0 < s < 1][0]
c_hat = [s for s in sp.solve(sp.Eq(1 - (1 - c) ** 2 / 2, r_res), c) if 0 < s < 1][0]
check("TM3", "memo point estimates imply a ~ 0.66 and c ~ 0.51 of a quarter",
      abs(float(a_hat) - 0.658) < 0.005 and abs(float(c_hat) - 0.510) < 0.005,
      f"start ~{float(a_hat) * 91:.0f} days before the ED; decision ~{float(c_hat) * 91:.0f} days "
      "before the ASU (variant R, uniform dates; Entering is imprecise, t = 0.19)")

# ---------------------------------------------------------------- Aggregation
from sympy.stats import Normal, variance

ep1, ep2, vp1, vp2 = sp.symbols("e1 e2 v1 v2", positive=True)
X1, X2 = Normal("X1", 0, sp.sqrt(vp1)), Normal("X2", 0, sp.sqrt(vp2))  # independent shocks
var_calc = sp.simplify(variance(ep1 * X1 + ep2 * X2))
check("A1", "firm reading variance = sum_p e_ip^2 sigma_p^2 (independent proposals)",
      sp.simplify(var_calc - (ep1**2 * vp1 + ep2**2 * vp2)) == 0,
      "for fixed PE = e1 + e2 it is largest when exposure is concentrated")
PE = sp.symbols("PE", positive=True)
v_conc = sp.simplify((e1**2 * v1 + e2**2 * v2).subs({e2: PE - e1, v1: 1, v2: 1}))
check("A2", "equal sigma: variance minimised at e1 = e2 = PE/2 for given PE",
      sp.solve(sp.diff(v_conc, e1), e1)[0] == PE / 2)

# ---------------------------------------------------------------- Contestedness
s2_bin = p * (1 - p) * D**2
check("C1", "binary outcome: sigma^2 = pi(1-pi) Delta^2, maximised at pi = 1/2 (inverted U)",
      sp.solve(sp.diff(s2_bin, p), p)[0] == sp.Rational(1, 2))

# ---------------------------------------------------------------- Commenting (optional)
gain_R = sp.simplify(A**2 / 2 - U_R.subs(I, IR))
check("B1", "value of removing rule risk (R) = (A^2/2) rho lam^2 s2/(1 + rho lam^2 s2)",
      sp.simplify(gain_R - A**2 / 2 * rho * lam**2 * s2 / (1 + rho * lam**2 * s2)) == 0,
      "increasing in lam and s2: exposed firms with short-horizon owners gain most")

# ---------------------------------------------------------------- Illustration
num = {g: sp.Rational(1, 4), lam: sp.Rational(3, 20), s2: sp.Rational(9, 100)}
drop_W = float(1 - dstar.subs(thbar, 0).subs(num))
print(f"\nIllustration (not a calibration): omega*b = 0.15, sd(theta) = 0.3, gamma = 0.25 "
      f"-> variant W postpones {drop_W:.1%} of pending-period investment")

print(f"\n{sum(results)}/{len(results)} checks pass")
