# Content and publishing

The existing README is unchanged. Its content is now displayed under Mathematics. All original notes, PDFs, and verification files retain their paths. The second website is read only; seven content pages and five project summaries were migrated from its TSX source into static Jekyll pages. Decorative graphics, animations, header taglines, and Back controls were removed. Research Interests on the biography page is titled Additional Background; the requested current interests appear on the homepage. The Deutsch Conversation App has no detail page in the source, so its summary is retained without a broken link.

Both original email addresses remain. The contact form now opens a draft addressed to the actual Outlook address displayed on that page instead of the source's example.com placeholder. It does not claim that a message has been sent.

The CV markup is retained but disabled with `show_cv: false` in `_config.yml`. Enable it after supplying the revised `folder/CV.pdf`. The Master's Project and Course Catalog sections were removed at the user's request; existing PDF paths are retained. Notes from Papers uses the shorter heading while retaining its previous fragment as an alias. Businesses is now presented as Ventures, retaining `/businesses/`. The standalone primespectrum page's missing local stylesheet/feed references were replaced with the shared stylesheet and generated feed.

Business links are stored in `_data/businesses.yml`. No business repository was accessed.

## Publishing articles

Create `_posts/YYYY-MM-DD-article-slug.md` with this front matter, then paste the article text unchanged below it:

```yaml
---
layout: post
title: "Exact article title"
date: YYYY-MM-DD
permalink: /articles/article-slug/
category: Guides
# Optional attribution and business links:
medium_url: https://medium.com/...
business_name: wavelocus.com
business_url: https://wavelocus.com
---
```

Set `medium_url` in `_config.yml` for a profile link on the article index. The supplied microphone-test article is included with its original prose and source links. Photographs, photograph links, photo credits, Medium interface controls, and the author byline are omitted at the user's request. Sitemap, feed, and SEO plugins remain enabled. No deployment was performed.
