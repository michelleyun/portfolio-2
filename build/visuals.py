# The Solution section of each case study: sub-headings, text and boxed visuals.
from html import escape as e


def table(head, rows, cls='tbl'):
    th = ''.join(f'<th scope="col">{e(h)}</th>' for h in head)
    body = ''.join('<tr>' + ''.join(f'<td>{e(c)}</td>' for c in r) + '</tr>' for r in rows)
    return f'<div class="scroll-x"><table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def fig(title, inner, note=''):
    n = f'<p class="note">{e(note)}</p>' if note else ''
    return f'<figure class="vis"><figcaption>{e(title)}</figcaption>{inner}{n}</figure>'


def tabs(uid, items):
    """items: list of (label, inner_html)"""
    tl = ''.join(
        f'<button type="button" role="tab" id="{uid}-t{i}" aria-controls="{uid}-p{i}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">{e(lab)}</button>'
        for i, (lab, _) in enumerate(items))
    ps = ''.join(
        f'<div role="tabpanel" id="{uid}-p{i}" aria-labelledby="{uid}-t{i}"{"" if i == 0 else " hidden"}>{inner}</div>'
        for i, (_, inner) in enumerate(items))
    return f'<div class="tabs"><div role="tablist" aria-label="Choose a view">{tl}</div>{ps}</div>'


def sub(h, *paras):
    return f'<h3>{e(h)}</h3>' + ''.join(f'<p>{e(p)}</p>' for p in paras)


# ---------- 01 ----------
def case01():
    segs = [
        ('Public-equity research', 'Monitor leadership changes across covered companies.', 'Identify developments that could influence investment research.', 'Company alerts, history, exports'),
        ('Event-driven investors', 'Screen for leadership turnover and corporate events.', 'Surface timely investment research opportunities.', 'Real-time alerts, executive-change screening'),
        ('Executive search & recruiting', 'Identify newly open roles and decision-makers.', 'Discover recruiting and business-development opportunities.', 'Role filters, company alerts'),
        ('Corporate strategy & advisory', 'Monitor leadership and compensation across a sector.', 'Support benchmarking and market intelligence.', 'Sector filters, compensation intelligence'),
    ]
    icp = tabs('icp', [(s[0], '<div class="trio">' + ''.join(
        f'<div><small>{lab}</small>{e(v)}</div>' for lab, v in zip(['Customer need', 'Value proposition', 'Relevant capabilities'], s[1:])) + '</div>') for s in segs])
    play = [
        ('Qualify', 'Prioritize relevant roles, recurring research needs, and trial engagement signals.'),
        ('Personalize', "Connect outreach to the buyer's sector, role, or a relevant leadership change."),
        ('Discover', 'Ask how they monitor changes today and what information would be most useful.'),
        ('Follow up', 'Introduce a different value point and offer a clear next step.'),
        ('Handle objections', 'Explore existing tools, frequency of need, and perceived value.'),
        ('Learn', 'Record use cases, feedback, and reasons for non-conversion to inform future outreach.'),
    ]
    steps = '<ol class="steps">' + ''.join(f'<li><span class="mono">{i + 1:02d}</span><b>{e(s)}</b>{e(t)}</li>' for i, (s, t) in enumerate(play)) + '</ol>'
    fb = table(['Research theme', 'Customer insight', 'Strategic opportunity'], [
        ('Conversion barriers', 'Existing subscriptions, infrequent needs, limited trial exploration, and budget considerations.', 'Refine qualification, onboarding, and competitive positioning.'),
        ('Feature preferences', 'Different workflows create different preferences for alerts, history, filters, and exports.', 'Develop audience-specific messaging and demonstrations.'),
        ('Audience fit', 'Research professionals, investors, and recruiters have distinct needs; recurring workflows offer clearer use cases.', 'Prioritize audiences with repeatable business needs.'),
        ('Product opportunities', 'Interest in personalization, context, coverage, and integrations.', 'Surface potential enhancements for product discussion.'),
        ('Product messaging', 'Practical workflow benefits matter more than information volume alone.', 'Communicate outcomes rather than listing features.'),
    ])
    return (sub('Audience segmentation & prioritization', 'Identified four priority customer segments through market research and assessed their use cases against existing trial-user profiles.')
            + fig('Ideal customer profile', icp)
            + sub('Competitive research & product positioning', 'Evaluated competing products and their market offerings. Mapped Succession’s capabilities to customer needs, informing value propositions tailored to each audience.')
            + sub('Sales enablement', 'Developed a structured sales playbook covering prospect qualification, personalized outreach, discovery conversations, follow-ups, and objection handling.')
            + fig('Sales playbook', steps)
            + sub('Voice of customer research', 'Interviewed trial users who had not converted to understand their current tools and workflows, feature preferences, unmet needs, and purchase considerations. This feedback will inform future product enhancements and commercial strategy.')
            + fig('Customer feedback', fb))


# ---------- 02 ----------
def case02():
    def dots(n):
        return f'<span class="dots" role="img" aria-label="{n} of 3">' + ''.join(f'<i class="{"on" if k < n else ""}"></i>' for k in range(3)) + '</span>'
    rows = [('Requirements coverage', 1, 2, 3), ('Ease of development', 3, 2, 1), ('Speed to market', 3, 2, 1), ('Product flexibility', 1, 2, 3)]
    head = '<tr><th scope="col"><span class="sr">Criteria</span></th><th scope="col">Use existing product</th><th scope="col">Extend existing product</th><th scope="col">Build a tailored product</th></tr>'
    body = ''.join(f'<tr><td>{e(r[0])}</td>' + ''.join(f'<td>{dots(v)}</td>' for v in r[1:]) + '</tr>' for r in rows)
    t = f'<div class="scroll-x"><table class="tbl trade"><thead>{head}</thead><tbody>{body}</tbody></table></div>'
    return (sub('Define the product opportunity', "I led discovery conversations with the partner to understand their objectives, the users the capability would serve, and how success would be measured. I translated these conversations into product requirements and prioritized them into must-have and nice-to-have capabilities.")
            + sub('Assess current product capabilities', 'I mapped each requirement against our existing product capabilities to identify what was already supported, what could be extended, and what would need to be built. This defined the scope of new development and gave us a baseline for comparing product approaches.')
            + sub('Evaluate the build path', 'Working with Product and Engineering, I developed alternative approaches for delivering the new capabilities and evaluated them against partner fit, implementation complexity, and development effort.')
            + fig('Approach trade-offs', t, 'More filled dots means a stronger rating, from 1 to 3.'))


# ---------- 03 ----------
def roadmap():
    W = [
        ('01', 'Platform Migration', '#b5c3ac', [('Discovery & requirements', 0, .6), ('Technical specification', .6, 1.3), ('Environment setup', 1.3, 2.0), ('Development testing', 2.0, 3.0), ('Production testing', 3.0, 3.8), ('Migration & cutover', 3.8, 4.6), ('General availability', 4.8, None)]),
        ('02', 'Measurement Expansion', '#a0b296', [('Discovery & requirements', .4, 1.0), ('Technical specification', 1.0, 1.7), ('Development testing', 2.0, 3.0), ('Production testing', 3.0, 3.8), ('Launch readiness', 3.8, 4.4), ('General availability', 4.6, None)]),
        ('03', 'New Product Integration', '#8ca081', [('Discovery & requirements', .8, 1.4), ('Technical specification', 1.4, 2.1), ('Initial product validation', 2.1, 3.0), ('Development testing', 3.0, 3.7), ('Production testing', 3.7, 4.4), ('Advertiser beta', 4.4, 5.2), ('Launch readiness', 5.2, 5.7), ('General availability', 5.85, None)]),
    ]
    pct = lambda m: f'{m / 6 * 100:.3f}%'
    out, y, pos = [], 30, {}
    head = ''.join(f'<span style="left:{(k + .5) / 6 * 100:.3f}%">Month {k + 1}</span>' for k in range(6))
    out.append(f'<div class="rm-r rm-h"><span></span><div class="rm-t">{head}</div></div>')
    for n, name, col, phases in W:
        out.append(f'<div class="rm-r rm-g"><span><span class="mono">{n}</span>{e(name)}</span><div class="rm-t"></div></div>')
        y += 38
        for lab, a, b in phases:
            if b is None:
                mark = f'<i class="ms" style="left:{pct(a)}" title="{e(lab)}"></i>'
            else:
                mark = f'<i class="bar" style="left:{pct(a)};width:{pct(b - a)};--w:{col}"></i>'
            out.append(f'<div class="rm-r"><span>{e(lab)}</span><div class="rm-t">{mark}</div></div>')
            pos[(n, lab)] = y + 13
            y += 26
    deps = [(('01', 'Environment setup'), ('02', 'Development testing'), 2.0),
            (('01', 'Development testing'), ('03', 'Development testing'), 3.0),
            (('02', 'Launch readiness'), ('03', 'Advertiser beta'), 4.4)]
    for s, t, x in deps:
        top, h = pos[s] + 5, pos[t] - pos[s] - 11
        out.append(f'<i class="dep" aria-hidden="true" style="left:calc(200px + (100% - 200px) * {x / 6:.4f});top:{top}px;height:{h}px"></i>')
    legend = '<div class="legend"><span><i class="lb"></i>Phase</span><span><i class="lm"></i>General availability</span><span><i class="ld"></i>Depends on</span></div>'
    return legend + '<div class="scroll-x"><div class="rm" role="img" aria-label="Six-month roadmap of three connected workstreams, each moving from discovery to general availability, with dependencies between them.">' + ''.join(out) + '</div></div>'


def stepper():
    st = [
        ('Stage 1', 'Define', 'Discovery, Technical specification', 'Gate 1', 'Ready to build', 'Validate',
         ['Scope, use cases and success criteria signed off', 'Technical spec and data requirements documented', 'Dependencies and owners identified'], 'Partner, Solutions Engineering'),
        ('Stage 2', 'Validate', 'Development testing, Production testing', 'Gate 2', 'Ready for beta', 'Launch',
         ['Test cases passed with no critical defects open', 'Production data matches expected results within agreed tolerance', 'Reporting validated end to end'], 'Engineering, Solutions Engineering'),
        ('Stage 3', 'Launch', 'Beta, General availability', 'Gate 3', 'Go / no-go', 'General availability',
         ['Beta acceptance criteria met and confirmed by the partner', 'Documentation and support teams ready', 'Monitoring and rollback plan in place'], 'Partner, Product, Solutions Engineering'),
    ]
    out = ''
    for s, name, ph, g, gname, nxt, crit, own in st:
        lis = ''.join(f'<li>{e(c)}</li>' for c in crit)
        out += (f'<div class="lstep"><div class="lrail"><i class="ldot"></i><i class="lln"></i></div><div>'
                f'<div class="lst"><small>{s}</small><b>{e(name)}</b><span>{e(ph)}</span></div>'
                f'<div class="gate"><div class="gt">{g} · {e(gname)} <span>→ {e(nxt)}</span></div><ul>{lis}</ul>'
                f'<p class="own">Sign-off: <b>{e(own)}</b></p></div></div></div>')
    return out


def case03():
    return (sub('Integrated program plan', 'I brought the three connected workstreams into a single roadmap, making phases, milestones, and dependencies visible across the program so potential risks and blockers could be identified and addressed early. I also created a centralized tracker that broke each workstream into actionable deliverables with clear owners and status, giving stakeholders a shared view of progress and accountability.')
            + fig('Integration roadmap', roadmap())
            + sub('Standardized testing and launch readiness', 'I formalized launch readiness criteria into clear checkpoints for each phase, with defined owners and sign-offs, giving all stakeholders shared visibility into when a workstream was ready to advance.')
            + fig('Launch readiness framework', stepper())
            + sub('Proactive risk management', 'I introduced a RAID log to track risks, assumptions, issues, and dependencies, and established a weekly internal meeting to review blockers, resolve open questions, and align on next steps.'))


# ---------- 04 ----------
def case04():
    demo = '''<div class="demo" id="demo">
<div class="dbar"><span class="logo">Advertiser reporting</span>
<label>Date range<select id="f-range"><option value="7">Last 7 days</option><option value="30" selected>Last 30 days</option></select></label>
<label>Channel<select id="f-chan"><option value="all">All</option><option>Display</option><option>Video</option><option>Mobile app</option></select></label>
<label>Campaign<select id="f-camp"><option value="all">All</option><option>Spring awareness</option><option>Product launch</option><option>Retargeting</option><option>Holiday promo</option></select></label></div>
<div class="kpis" aria-live="polite"><div><small>Impressions</small><b id="k-imp">11,280,934</b></div><div><small>Viewability</small><b id="k-v">72.4%</b></div><div><small>Brand safety</small><b id="k-b">96.2%</b></div><div><small>Invalid traffic</small><b id="k-i">1.2%</b></div></div>
<div class="scroll-x"><table class="tbl dt"><thead><tr><th scope="col">Campaign</th><th scope="col">Impressions</th><th scope="col" title="Share of ads that had a real chance to be seen">Viewability</th><th scope="col" title="Share of ads that ran next to suitable content">Brand safety</th><th scope="col" title="Share of traffic that came from bots or other non-human sources">Invalid traffic</th></tr></thead>
<tbody id="d-body"><tr><td>Spring awareness</td><td>1,989,765</td><td>70.7%</td><td>96.2%</td><td>1.2%</td></tr><tr><td>Product launch</td><td>2,495,226</td><td>71.3%</td><td>96.3%</td><td>1.2%</td></tr><tr><td>Retargeting</td><td>3,071,527</td><td>73.0%</td><td>96.0%</td><td>1.2%</td></tr><tr><td>Holiday promo</td><td>3,724,416</td><td>73.6%</td><td>96.2%</td><td>1.2%</td></tr></tbody></table></div>
<p class="note">Change a filter: every total, rate and row recalculates from the same underlying data.</p></div>'''
    return (sub('Interactive product demo', 'A shareable, interactive product demo that allowed the partner to explore the reporting experience without requiring platform access or exposing real advertiser data. The prototype recreated key elements of the advertiser experience: reporting dashboards, interactive filters and dropdown menus, metric definitions and tooltips, and reporting tables and data exports.')
            + sub('Realistic, partner-specific data', 'Because each partner’s advertisers see different inventory, metrics, and performance ranges, I built a synthetic dataset modeled on this partner’s environment. The data stayed consistent across every view, so filters, totals, and metric definitions behaved as they would in a live account, giving the partner a credible preview of what their advertisers would actually see.')
            + fig('Prototype preview', demo))


# ---------- 05 ----------
def bars(title, rows):
    rs = ''.join(f'<div class="br"><span>{e(l)}</span><span class="tr"><i class="fl" style="width:{v / 200 * 100:.1f}%"></i><i class="base" style="left:50%"></i></span><b>{v}</b></div>' for l, v in rows)
    return f'<p class="ct">{e(title)}</p><div class="bars">{rs}</div><p class="key">Index values. The dashed line is 100, the average consumer.</p>'


def interp(t):
    return f'<p class="in"><b>Interpretation</b>{e(t)}</p>'


def case05():
    strat = [('Core audience', 'Technology enthusiasts and sustainability-minded consumers.'),
             ('Expansion audience', 'Hybrid vehicle shoppers; emphasize range and charging convenience.'),
             ('Campaign timing', 'Test messaging around Earth Day and spring auto-shopping season.'),
             ('Measurement', 'Evaluate response and refine targeting.')]
    st = '<p class="ct">Recommended audience strategy</p><ol>' + ''.join(f'<li><b>{e(a)}:</b> {e(b)}</li>' for a, b in strat) + '</ol>'
    t = tabs('brief', [
        ('Audience', bars('Interests of prospective EV buyers', [('Clean energy', 185), ('Consumer technology', 162), ('Hybrid vehicles', 148), ('Outdoor recreation', 135), ('Personal finance', 124)])
         + interp('Prioritize technology enthusiasts and sustainability-minded consumers; test hybrid vehicle shoppers as an adjacent audience.')),
        ('Competitors', bars('EV purchase interest by audience segment', [('Technology enthusiasts', 148), ('Hybrid vehicle shoppers', 125), ('General auto shoppers', 112)])
         + interp('Technology enthusiasts show stronger relative interest, while hybrid shoppers offer an additional audience to test.')),
        ('Trends', bars('EV research interest over time', [('Jan', 100), ('Feb', 112), ('Mar', 108), ('Apr', 135), ('May', 148), ('Jun', 162)])
         + interp('In this example, rising spring interest suggests testing campaigns around Earth Day and the spring auto-shopping season.')),
        ('Strategy', st),
    ])
    brief = ('<div class="brief"><p class="eb">Audience research · Automotive</p><h4>Who is the next electric vehicle buyer?</h4>'
             '<p class="bq">Which audiences should an automotive brand target for an electric vehicle campaign?</p>' + t + '</div>')
    return (sub('Audience research and media recommendations', 'I translated research findings into client-facing presentations that combined data visualizations, consumer insights, and actionable recommendations. These included audience profiles, competitive comparisons, and trend analysis, tailored to the client’s business objectives.')
            + fig('Audience strategy brief', brief))


# ---------- 06 ----------
def case06():
    st = [('The issue', 'Behind target', "Halfway through the test, one of the client's success metrics was below its goal."),
          ('Root cause', 'One filter', 'Most of the shortfall came from a single content filter that was set too strictly.'),
          ('The insight', 'Blocking the right audience', 'The filter was screening out the exact content the client wanted to reach.'),
          ('The fix', 'On track to target', 'Two adjustments to the filter settings were projected to bring results back within the goal.')]
    r = '<ol class="rca" style="list-style:none;margin:0;padding:0">' + ''.join(
        f'<li><div><i class="nd{" on" if i == 3 else ""}" aria-hidden="true"></i><small>{i + 1} · {e(a)}</small><b>{e(b)}</b><p>{e(c)}</p></div></li>' for i, (a, b, c) in enumerate(st)) + '</ol>'
    return (sub('Centralized performance tracking', 'I created a centralized campaign performance tracker to provide Sales, Solutions Engineering, and senior leadership with visibility into the evaluation. Updated daily, the tracker consolidated performance metrics, benchmark comparisons, key findings, and configuration changes, making it easier for stakeholders to understand campaign progress without having to pull individual reports.')
            + sub('Performance analysis and optimization', 'I translated campaign data into actionable recommendations, identifying the drivers of performance fluctuations and opportunities for improvement. I developed and presented mid-campaign findings to the customer, explaining performance trends, recommending configuration changes, and demonstrating how our products could better support their objectives.')
            + fig('Root cause analysis', r))


SOLUTIONS = [case01, case02, case03, case04, case05, case06]
