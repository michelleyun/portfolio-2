# All site copy, taken from the portfolio handoff. Case study wording is final: use as is.

SITE = 'https://michelleyun.github.io/portfolio-2/'
EMAIL = 'michelleyoungyun@gmail.com'
LINKEDIN = 'https://www.linkedin.com/in/michelleyun5'
LINE = 'I turn technical complexity into clear plans and measurable outcomes.'

CASES = [
    dict(n='01', slug='01-go-to-market', tag='Go-to-market',
         title='Building a go-to-market strategy from the ground up',
         line='Connecting product capabilities with market needs through audience segmentation, sales enablement, and firsthand customer research.',
         company='Succession', role='Go-to-market consultant', deliverable='Go-to-market strategy & sales playbook',
         challenge='A useful product with no defined audience, positioning, or sales strategy.',
         did='Researched the market, prioritized four customer segments, positioned the product, built a sales playbook, and interviewed trial users.',
         outcome='Established a foundational go-to-market strategy that attracted early paying customers, and surfaced the adoption barriers and product needs shaping the commercial opportunity.',
         context='Succession is a financial intelligence platform that tracks executive and board leadership changes in real time by aggregating information from SEC filings and press releases. Originally developed for personal use, the platform had potential to serve a broader commercial market. The challenge was to identify which audiences had a need for this information, understand their unique needs, and communicate the value.',
         approach='I combined market and competitive analysis with direct customer discovery. I assessed potential customer segments against their needs and existing trial-user profiles, then interviewed trial users who had not converted to understand their workflows, unmet needs, and barriers to adoption.',
         impact=[('GTM strategy', 'Defined four potential customer segments, developed audience-specific positioning, and created a structured sales playbook.'),
                 ('Customer insight', 'Identified adoption barriers and product needs through trial-user interviews.'),
                 ('Early commercial traction', 'The product attracted paying customers, providing an initial signal of willingness to pay.')]),
    dict(n='02', slug='02-product-strategy', tag='Product strategy',
         title='Defining what to build for a strategic partner',
         line='Turning an ambiguous partner request into clear requirements, solution options, and product opportunities.',
         company='Integral Ad Science', role='Solutions Engineer', deliverable='Product assessment & solution design',
         challenge='A strategic platform partner had a need that our existing products could not fully address. We needed to define the requirements and determine what product capabilities to build.',
         did='Led discovery with the partner, translated its needs into product requirements, assessed current capabilities and gaps, and worked with Product and Engineering to compare alternative approaches.',
         outcome='Defined product direction and the capabilities needed to address the partner’s requirements.',
         context='A strategic platform partner was exploring new product capabilities as part of a competitive opportunity. Their requirements extended beyond our existing product offerings, so we needed to define what new capabilities to build and how they would fit alongside our current products.',
         approach="I started by understanding the partner's objectives and expected functionality, then translated them into product requirements. Using our existing capabilities as a baseline, I defined what needed to be built and worked with Product and Engineering to scope and compare approaches.",
         impact=[('Product requirements', "Translated the partner's need into clear, prioritized product requirements."),
                 ('Build scope', 'Identified which capabilities to extend and which to build new.'),
                 ('Product direction', "Recommended an approach that met the partner's needs and fit within the existing product portfolio.")]),
    dict(n='03', slug='03-program-management', tag='Program management',
         title='Building a better way to manage technical integrations',
         line='Managing interconnected product initiatives, technical dependencies, and cross-functional launch readiness.',
         company='Integral Ad Science', role='Solutions Engineer', deliverable='Integration management framework',
         challenge='Technical partner integrations lacked a consistent project-management process, making ownership, dependencies, and launch readiness difficult to manage across teams.',
         did='Created an integrated roadmap and tracker, formalized launch-readiness criteria, and established a weekly review of risks and dependencies across connected workstreams.',
         outcome='Clearer ownership and earlier risk detection, and adoption of the framework across Solutions Engineering organization.',
         context='Technical integrations often involved several connected workstreams, but there was no consistent process for managing them. During one partner initiative, separate plans and milestones made it difficult to track overall progress, ownership, and dependencies.',
         approach='I designed a full integration lifecycle process for coordinating three interconnected workstreams as one program. My goal was to both improve delivery of the current integration and give future integrations a more efficient, repeatable foundation.',
         impact=[('Workstream coordination', 'Improved accountability and coordination across teams.'),
                 ('Proactive risk management', 'Earlier identification of blockers and better alignment on deadlines.'),
                 ('Cross-team adoption', 'A reusable framework adopted across Solutions Engineering.')]),
    dict(n='04', slug='04-ai-prototyping', tag='AI prototyping',
         title='Bringing a product experience to life with AI',
         line='Using AI-assisted development to build an interactive prototype with realistic, partner-specific data.',
         company='Integral Ad Science', role='Solutions Engineer', deliverable='Interactive product demo',
         challenge='A partner wanted to explore the advertiser reporting experience, but there was no interactive demo and real advertiser data could not be shared.',
         did='Used generative AI to turn existing product designs into a browser-based prototype with synthetic data, building and refining it without dedicated engineering support.',
         outcome='The partner could explore the advertiser reporting experience firsthand, without needing platform access or real data.',
         context='A platform partner wanted to understand how advertisers would experience the reporting platform and asked for screenshots or a video walkthrough. Static screenshots would not truly show how the product worked, and a live demo using real advertiser data was not an option.',
         approach='I wanted to give the partner a useful way to evaluate the product, rather than just send static screens. My goal was to make the experience as realistic and explorable as possible, using data that reflected the partner’s environment, while protecting real data.',
         impact=[('Rapid prototyping', 'From concept to functional product demo.'),
                 ('Data privacy', 'Realistic, partner-specific data without exposing any real advertiser information.'),
                 ('Hands-on evaluation', 'Let the partner test real workflows instead of reviewing static screens.')]),
    dict(n='05', slug='05-consumer-insights', tag='Consumer insights',
         title='Turning consumer insights into actionable marketing strategies',
         line='Using consumer research to help brands identify audience opportunities and inform marketing strategy.',
         company='Nexxen', role='Analyst, Advanced Insights & Data', deliverable='Client-facing research presentations',
         challenge='Sales needed research-backed collateral to open prospect conversations, while clients needed audience insights to inform media strategy.',
         did='Analyzed consumer interests, behaviors, demographics, and trends, then translated the findings into client presentations to inform media buying strategies.',
         outcome='Research that helped Sales open conversations and helped brand and agency teams plan campaigns.',
         context='At Nexxen, my research supported both new business conversations and campaign planning. Sales used tailored research presentations to start conversations with prospects about their customers and market. For brand and agency teams planning a media buy, the research provided a basis for deciding which audiences to prioritize and why.',
         approach='I worked with Sales to understand what each client wanted to learn, then used a proprietary consumer intelligence platform and indexed scores to compare segments, find what made audiences distinct, and spot timely trends.',
         impact=[('Sales enablement', 'Strategic materials for opening conversations with prospective clients.'),
                 ('Audience strategy', 'Clear recommendations on who to target and why.'),
                 ('Market intelligence', 'Timely insights into emerging trends and major events.')]),
    dict(n='06', slug='06-competitive-strategy', tag='Competitive strategy',
         title='Winning a head-to-head evaluation against an incumbent',
         line='Leading a head-to-head evaluation from testing methodology and customer enablement to optimization and commercial storytelling.',
         company='Integral Ad Science', role='Solutions Engineer', deliverable='Test design & performance optimization',
         challenge='A high-stakes head-to-head evaluation to displace an incumbent competitor.',
         did='Designed the testing methodology, tracked performance daily in a central tracker and presented mid-campaign recommendations.',
         outcome='Demonstrated product and partnership value, resulting in a competitive win.',
         context='Given their revenue potential, head-to-head product evaluations receive heightened scrutiny from both customers and internal leadership. Success requires more than strong product performance. It also requires a well-designed testing methodology, ongoing performance monitoring, and a strong customer partnership.',
         approach='Using the advertiser’s success criteria, I designed the testing methodology and recommended the products, configurations, and implementation approach best suited to achieving their objectives.',
         impact=[('New business win', 'Demonstrated product and partnership value against an incumbent competitor leading to a win.'),
                 ('Customer trust', 'Strengthened the relationship by acting as a hands-on partner throughout the evaluation.'),
                 ('Leadership visibility', 'Centralized performance insights for leadership to inform commercial decisions.')]),
]

PHOTOS = [
    ('01-henry.jpg', 'Henry', 'North Ave Beach, Chicago', '85mm', 'Henry mid-jump against the Chicago skyline.'),
    ('02-clover.jpg', 'Clover', 'Chicago', '50mm', 'Clover, a fluffy wheaten puppy, running through grass.'),
    ('03-kj-chicago-suburbs.jpg', 'KJ', 'Chicago suburbs', '85mm', 'KJ, a black-and-tan doodle in a red bandana, in tall grass.'),
    ('04-poppy.jpg', 'Poppy', 'The Honeycomb, Chicago', '50mm', 'Poppy, a cream-colored dog with a pink bow.'),
    ('05-josie.jpg', 'Josie', 'Lincoln Park, Chicago', '35mm', 'Josie, a chocolate doodle with a pink bow, running with the skyline behind.'),
    ('06-henry-and-kj.jpg', 'Henry & KJ', 'Montrose Beach, Chicago', '35mm', 'Henry and KJ, two doodles in bandanas, on the beach.'),
    ('07-gus.jpg', 'Gus', 'Chicago', '50mm', 'Gus, a golden dog, in a leafy garden.'),
    ('08-scout.jpg', 'Scout', 'Chicago suburbs', '85mm', 'A warmly lit close-up of Scout, a brown and white dog.'),
    ('09-kj-houston.jpg', 'KJ', 'Houston', '85mm', 'KJ framed by green foliage.'),
    ('10-maja.jpg', 'Maja', 'Lincoln Park, Chicago', '50mm', 'Maja, a black dog with a red bow, among yellow flowers.'),
]

ABOUT = [
    "I started my career in consumer intelligence, helping brands and agencies understand their audiences and make more informed marketing decisions. I then moved into solutions engineering, where I work closely with customers, product teams, engineers, and commercial stakeholders.",
    "What I enjoy most is figuring things out — whether that's understanding a customer problem, identifying patterns in data, bringing structure to a complex project, or exploring a new technology.",
    "Outside of work, you'll usually find me playing tennis, cooking, taking photos, or spending time with my dog, KJ.",
]
ABOUT_LEAD = "I'm a Chicago-based professional with seven years of experience across audience research, data analytics, and solutions engineering."

BACKGROUND = [
    ('Experience', [
        ('Integral Ad Science', 'Solutions Engineer', 'Jun 2025 – Present', True, None),
        ('Nexxen (formerly Amobee)', 'Solutions Engineer, Enterprise', 'Aug 2021 – Apr 2025', False, None),
        ('Nexxen (formerly Amobee)', 'Analyst, Advanced Insights & Data', 'Aug 2019 – Aug 2021', False, None)]),
    ('Independent projects', [
        ('Succession', 'Go-to-Market Consultant', 'Aug 2025 – Present', True, ('Case study ↗', 'work/01-go-to-market.html')),
        ('Michelle Yun Photography', '', 'Jun 2019 – Present', True, ('Photography ↗', 'photography.html'))]),
    ('Education', [
        ('Northwestern University', 'B.A. Communication Studies, concentration in Integrated Marketing Communications', 'Sep 2015 – Jun 2019', False, None)]),
]

TOOLKIT = [
    ('Product & Strategy', [('Product discovery', '02'), ('Audience segmentation', '01'), ('GTM strategy', '01'), ('Competitive positioning', '06'), ('Voice-of-customer research', '01'), ('Requirements & gap analysis', '02')]),
    ('Data & Insights', [('Consumer intelligence', '05'), ('Performance analysis', '06'), ('Data visualization', '05'), ('SQL & Databricks', None), ('Tableau', None), ('Excel & Google Sheets', None)]),
    ('Program & Execution', [('Cross-functional coordination', '03'), ('Project planning', '03'), ('Stakeholder management', '02'), ('Risk & dependency management', '03'), ('Testing & validation', '03'), ('Launch readiness', '03')]),
    ('Technology & Innovation', [('Technical integration scoping', '03'), ('API testing & troubleshooting', None), ('Technical documentation', '03'), ('Solution design', '02'), ('Data validation', '03'), ('AI-assisted prototyping', '04')]),
]
