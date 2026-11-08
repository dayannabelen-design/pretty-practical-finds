# Pretty Practical Finds — November 8, 2026 editorial work

Status: drafts and audit only. No Netlify or social publication in this run.

## Live audit

Checked the canonical Netlify site's sitemap, all 13 listed URLs, robots.txt and page HTML on November 8, 2026.

- All 13 listed pages returned HTTP 200.
- Each page has one H1, a unique title and description, and a self-referencing canonical on https://prettypractical.netlify.app.
- No old clever-hotteok domain references were found in the 13 HTML documents.
- robots.txt permits crawling and points to the correct sitemap.
- All root-relative internal page destinations found in the HTML resolve to sitemap-listed paths. Fragment targets and external links were not exhaustively checked.
- All image elements have alt attributes; this does not establish that every description is sufficiently specific.
- Structured-data JSON parsed on every page containing it. This is not a Google rich-result eligibility test.
- The recipes hub is missing og:url. Add the snippet below at the next authorized Netlify deployment.
- No external analytics scripts were found in the scanned HTML. This does not rule out server-side Netlify analytics.
- Search impressions, affiliate clicks, orders, commissions and social reach are unavailable in this run. They are not reported as zero.
- GitHub main is substantially older than Netlify (four HTML pages versus 13 sitemap URLs). Do not deploy GitHub main over Netlify or replace current site files with the old fallback.
- Escali Primo already has a paid link in the live scale guide: ASIN B0007GAWRS, tracking tag theprettypr0a-20, rel sponsored, an introductory disclosure and a disclosure beside the link. The untagged Amazon destination was checked against its Escali Primo product title. No test affiliate click was generated.
- Prior session evidence confirmed the new public Netlify URL in Associates. No new paid links were added today.

### Metadata patch for /recipes

Keep the existing canonical. Add inside head, after checking no duplicate tags exist:

```html
<meta property="og:url" content="https://prettypractical.netlify.app/recipes">
```

### Access required to publish

Netlify project dashboard shows its login form. Facebook shows a login dialog and Pinterest shows Log in / Sign up. These cloud sessions do not inherit the signed-in desktop sessions used for earlier publishing. No credentials were requested during this unattended work.

Needed connections: authenticated Netlify deployment access for project prettypractical; authenticated Facebook Page publishing access for ThePrettyPractical; an authenticated Pinterest account and destination board. Search Console and Amazon reporting access are separately needed for measurement.

## Search research and editorial choice

Queries researched today: “Escali Primo bread baking scale small yeast amounts accuracy” and “sourdough starter not rising day 3 day 4,” with a second search for manufacturer and King Arthur sources.

Real reader questions in search results:
- A Breadit user described a scale remaining at 0 g while yeast was added: https://www.reddit.com/r/Breadit/comments/1vvox99/decent_kitchen_scale/
- A new starter owner described activity on day three followed by no rise after the next feeding: https://www.reddit.com/r/SourdoughStarter/comments/1x03cs4/sourdough_starter_not_rising/
- Another described a day-four stall and began changing feeding ratios: https://www.reddit.com/r/SourdoughStarter/comments/1rvqvb6/my_sourdough_starter_wont_rise_since_day_4/

These are qualitative question signals, not keyword-volume estimates or evidence of this site's traffic.

Editorial decision: expand the existing scale guide rather than create a competing “best scale” page. Prepare a focused starter troubleshooting article that complements, rather than repeats, /sourdough-starter-basics. The gift and starter-basics pages were already added November 7; do not publish daily just to fill a quota. Aim next for two useful articles and two or three social posts/pins during the coming week, after checking recent posts and available results.

## Ready-to-insert scale-guide improvement

Placement: replace the current “Two things to check before choosing the Escali Primo” section, retaining its anchor ID and existing paid-link disclosure.

### Is the Escali Primo enough for your bread baking?

A scale has two jobs at the mixing bowl: carry the whole batch and show useful changes as you add ingredients. Those are different questions.

The manufacturer's current Primo page lists a maximum load of 5,000 g (11 lb), tare and automatic shutoff after four minutes of inactivity. That capacity includes the bowl. A heavy mixing bowl does not become weightless when you press zero.

Before buying, set your usual bowl on your current scale and note its empty weight. Add up the ingredient weights for the largest recipe you actually make. The bowl and the batch both need to fit within the new scale's capacity. Check the display position too: an enormous bowl can turn a perfectly readable screen into a game of peekaboo.

For small yeast doses, look beyond a promise of “precise weighing.” A display that changes in whole grams cannot show 2.5 g. More decimal places are not, by themselves, proof of accuracy either. Choose a tool with a stated range and accuracy suitable for that quantity, or follow the recipe's supplied spoon measure.

The Primo is an option to compare for everyday mixing. It is not a promise that every pinch, bowl or doubled recipe will suit it. We have not performed a hands-on test of this model.

Source checked November 8: https://kitchensupply.com/products/primo-digital-scale
Keep current affiliate button unchanged until the next verified deployment. Do not add current prices, customer ratings or an invented testing badge.

## Full article draft — not published

Proposed path: /sourdough-starter-not-rising
SEO title: Sourdough Starter Not Rising? Check These Things First
Meta description: A quiet sourdough starter isn't always a failed one. Check its age, feeding routine and temperature, then learn when to wait and when to start over.
Canonical after publication: https://prettypractical.netlify.app/sourdough-starter-not-rising
Schema: BlogPosting plus BreadcrumbList. No Recipe, Review or aggregateRating markup.
Author: use the site's established author identity; do not invent credentials.
Image: commission an original jar-and-notebook illustration or use an owner-supplied starter photo. Do not label a generated jar as evidence of a tested feeding routine.

# Sourdough starter not rising? Before you give your jar a dramatic farewell

Yesterday, the jar seemed full of ambition. Today, you lift the lid, peer at a few sleepy bubbles and wonder whether you have somehow offended flour.

That quiet afternoon does not necessarily mean your starter has failed. A brand-new culture, a cold kitchen and an established starter overdue for a meal need different responses. Before changing the flour, feeding ratio and resting spot all at once, work out which situation is sitting on your counter.

**Start here:** note your starter's age, its most recent feeding, the room temperature and whether it rises and falls between checks. That short record is more useful than refreshing someone else's day-five photograph.

## First, how old is the starter?

A starter that bubbled enthusiastically during its first few days is still developing. King Arthur Baking explains that a new starter can show an early rise and then remain quiet for a week or longer, even with regular feeding.

So a day-four lull is not, by itself, a reason to throw everything away. Keep following a reliable starter method rather than treating one lively afternoon as proof that the culture was ready for bread.

New to the process? Read our [starter basics and feeding-ratio guide](/sourdough-starter-basics) alongside the complete starter recipe you are following.

## Give your next observation a starting line

A jar without a mark is surprisingly hard to read. Put a rubber band at the starter's level immediately after feeding, or mark the outside of the jar. Leave room above it for expansion.

Write down the time. When you return, look for a higher level, fresh bubbles and a residue line above the current mixture. A starter may have risen while you were busy and settled before you checked it. A clean, straight-sided container makes those changes easier to see.

You do not need a new matching jar set to begin. The point is to make the change visible.

## Check the room before blaming the recipe

A chilly counter can slow fermentation. King Arthur notes that temperatures below 68°F can make a starter take considerably longer to rise.

Check the temperature near the jar instead of assuming the whole kitchen feels the same. If you move it somewhere warmer, avoid direct heat and monitor that spot. A cozy corner should not become a hot cupboard. Do not put the jar somewhere that another person may switch on an appliance without noticing it.

Record the new location before changing anything else. Otherwise, tomorrow's improvement will come with a small mystery attached: was it the flour, the water, the ratio or the new shelf?

## Make the feeding ratio a weight ratio

Equal parts starter, flour and water means equal weights, not three equal scoops. A cup of bubbly starter changes with its texture and how much it has been stirred down; weight gives you a more repeatable starting point.

For example, a 1:1:1 feeding can mean 30 g starter, 30 g flour and 30 g water. This illustrates the ratio, not a separate starter-creation schedule. Keep the timing and method consistent with the reliable recipe you chose.

Use our [kitchen-scale guide](/digital-kitchen-scale-bread) if tare still feels like a button you are slightly afraid to press.

## Bubbles are encouraging. Bread needs reliable lifting power.

A few bubbles do not tell you how well a starter will lift dough. King Arthur's creation guide uses a repeated doubling within roughly six to eight hours after feeding as a readiness benchmark. Conditions matter; the calendar alone is not the test.

Watch several feedings instead of announcing victory after one impressive rise. If your starter is thin enough that bubbles simply escape through it, check the flour-and-water proportions in your method before adding another random scoop.

And if you want bread today while your jar takes its time, choose a recipe that uses commercial yeast. Our [evaporated-milk sandwich bread](/evaporated-milk-sandwich-bread) is a separate baking project, not a shortcut for declaring an immature starter ready.

## When to stop trying to revive it

Visible mold, pink or orange discoloration, or a putrid odor call for discarding the starter and beginning again. Do not scrape off a suspicious patch and use the mixture underneath. A normal sour or yeasty aroma is different from spoilage.

A slow jar can deserve patience. A contaminated jar does not need a rescue story.

## What should you do at the next feeding?

Keep the plan small: inspect the starter, follow your chosen feeding method, mark its starting level and note the time and temperature. Give yourself something clear to compare at the next check.

The goal is not a beautiful photograph on exactly the right day. It is a starter whose behavior you can recognize—and, eventually, trust with a bowl of dough.

### Reader questions

**It rose on day two and stopped. Did I kill it?** An early rise followed by a lull can occur during starter development. Age and continued progress matter more than one day's height.

**Can I measure the feeding with equal cups?** Not for a ratio specified by weight. Weigh each component.

**Should I buy a starter warmer first?** Check the actual temperature and your routine before buying equipment. This guide does not require a purchase.

Sources for editor verification and article references:
1. https://www.kingarthurbaking.com/blog/2024/12/19/why-is-my-sourdough-starter-not-rising — early lull and temperature.
2. https://www.kingarthurbaking.com/learn/guides/sourdough/maintain — weighing starter and consistent maintenance.
3. https://www.kingarthurbaking.com/learn/guides/sourdough/create — readiness, observation and contamination signs.
4. https://www.kingarthurbaking.com/learn/guides/sourdough/faq — discard criteria.

Before publication: add the new page to sitemap only once live; add one contextual link from starter basics; keep the basics page's broader feeding focus. Use the actual publication date and a real image, not placeholder metadata. Test mobile formatting and every link.

## Ready-to-use Facebook drafts

Do not repost yesterday's gift collage. Check the Page's latest posts before using these.

### Scale guide — first available slot

#ad · The linked guide contains paid links. As an Amazon Associate I earn from qualifying purchases.

The bowl is on the scale. You press zero. Someone asks where their shoes are.

When you return, zero is still zero—but the bowl still counts toward the scale's weight limit. A tiny detail that matters when you're doubling bread dough. 🤎

Our guide walks through tare, keeping your place, and why tiny yeast amounts need a different approach.

https://prettypractical.netlify.app/digital-kitchen-scale-bread?utm_source=facebook&utm_medium=organic_social&utm_campaign=scale_basics

Which baking step always seems to get interrupted in your kitchen?

#BreadBaking #KitchenScale #BakingTips

### Starter basics — second available slot

Your starter has a name. A favorite spot on the counter. Possibly more attention than the houseplants.

But what does 1:1:1 actually mean?

Equal weights of starter, flour and water—not three matching scoops. Our beginner guide makes feeding ratios feel a little less like homework. 🌿

https://prettypractical.netlify.app/sourdough-starter-basics?utm_source=facebook&utm_medium=organic_social&utm_campaign=starter_basics

What's the one starter question you wish someone had explained sooner?

#SourdoughStarter #SourdoughBeginners #BreadBaking

### Recipe box — optional third slot, only if cadence allows

A loaf for toast. A loaf to freeze. A loaf that may not survive long enough to be either. 🤎

If a slow baking afternoon sounds good, the recipe box is open: banana bread in grams and evaporated-milk sandwich bread, with pan notes and printable cards.

https://prettypractical.netlify.app/recipes?utm_source=facebook&utm_medium=organic_social&utm_campaign=recipe_box

What would you bake first?

#HomemadeBread #BananaBread #BakingRecipes

## Pinterest copy and original visual briefs

Use an original illustration or user-owned image. These briefs do not authorize copying product photography. Board suggestions are categories, not verified existing boards. No pins have been published.

### Pin 1 — scale guide

Title: How to Use a Kitchen Scale for Bread Baking
Description: Learn the tare routine, why bowl weight still counts toward capacity, and what to check for small yeast measurements. Paid links in the guide. As an Amazon Associate I earn from qualifying purchases.
Destination: https://prettypractical.netlify.app/digital-kitchen-scale-bread?utm_source=pinterest&utm_medium=organic_social&utm_campaign=scale_basics
Overlay: The bowl still counts.
Subline: A little guide to tare & bread baking
Board category: Bread Baking Tips
Visual: 1000×1500 cream background, original line illustration of a mixing bowl above a scale; sage border and berry headline. Do not draw a branded model or a fabricated measurement result.
Alt: Illustration of a mixing bowl on a kitchen scale with a reminder that the bowl counts toward the total load.

### Pin 2 — starter basics

Title: Sourdough Starter Feeding Ratios, Simply Explained
Description: A friendly introduction to feeding sourdough starter by weight, including what a 1:1:1 ratio means. Start with the basics before shopping for more equipment.
Destination: https://prettypractical.netlify.app/sourdough-starter-basics?utm_source=pinterest&utm_medium=organic_social&utm_campaign=starter_basics
Overlay: 1:1:1 without the overwhelm
Subline: Starter · Flour · Water, by weight
Board category: Sourdough for Beginners
Visual: Original botanical border and three hand-drawn labeled bowls. Use equal-weight language; do not imply equal volumes.
Alt: Three illustrated bowls labeled starter, flour and water, with a note that a 1:1:1 feeding uses equal weights.

### Pin 3 — recipe hub

Title: Cozy Bread Recipes With Gram Measurements
Description: Find banana bread and evaporated-milk sandwich bread recipes with practical pan notes and printable recipe cards in the Pretty Practical Finds recipe box.
Destination: https://prettypractical.netlify.app/recipes?utm_source=pinterest&utm_medium=organic_social&utm_campaign=recipe_box
Overlay: Put the kettle on. Let's bake.
Subline: Open the recipe box
Board category: Homemade Bread Recipes
Visual: Use an owner-supplied bread photo already cleared for reuse, or an original recipe-card illustration. Never present generated bread as a tested recipe result.
Alt: Use an accurate description of the final chosen photo or illustration.

## Measurement log to fill when reporting access is connected

Record weekly: Search Console clicks, impressions, query and landing page; Facebook link clicks/reach; Pinterest outbound clicks/impressions; Associates clicks, ordered items, shipped items and commissions, with the date range.
UTMs distinguish social referrals on the website; they do not independently measure Amazon commissions.
Do not invent a new Associates tracking ID. If the shared existing tag remains in use, report its actual aggregate results and acknowledge the attribution limit.
No ads, purchases, subscriptions, outreach or fake engagement were used.
