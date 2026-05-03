import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [
    Component.ConditionalRender({
      condition: (page) => page.fileData.slug === "index",
      component: Component.RecentNotes({
        title: "🗓 Latest Events",
        limit: 3,
        filter: (f) => f.slug !== undefined && f.slug.includes("Events") && !f.slug.endsWith("index"),
      }),
    }),
    Component.ConditionalRender({
      condition: (page) => page.fileData.slug === "index",
      component: Component.RecentNotes({
        title: "🛠 Featured Services",
        limit: 4,
        filter: (f) => {
          if (!f.slug || f.slug.endsWith("index")) return false
          // Include items under Services/ but exclude Classes and Tutoring subfolders
          return f.slug.includes("Services") &&
            !f.slug.includes("Classes") &&
            !f.slug.includes("Tutoring")
        },
      }),
    }),
    Component.ConditionalRender({
      condition: (page) => page.fileData.slug === "index",
      component: Component.RecentNotes({
        title: "📚 Classes & Tutoring",
        limit: 4,
        filter: (f) => {
          if (!f.slug || f.slug.endsWith("index")) return false
          return f.slug.includes("Classes") || f.slug.includes("Tutoring")
        },
      }),
    }),
    Component.ConditionalRender({
      condition: (page) => page.fileData.slug === "index",
      component: Component.RecentNotes({
        title: "🛒 Products",
        limit: 3,
        filter: (f) => f.slug !== undefined && f.slug.includes("Products") && !f.slug.endsWith("index"),
      }),
    }),
  ],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/jackyzha0/quartz",
      "Discord Community": "https://discord.gg/cRFFHYye7t",
    },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),

    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer(),
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer(),
  ],
  right: [],
}
