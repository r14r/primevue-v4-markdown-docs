# Dock

Dock is a navigation component consisting of menuitems.

## Import [#](https://primevue.org/dock/#import)

```

import Dock from 'primevue/dock';


```

## Basic [#](https://primevue.org/dock/#basic)

Menu requires a collection of menuitems as its *model* and an *icon* template. Default location is *bottom* and other edges are also available when defined with the *position* property.

Bottom

Top

Left

Right

```

<Dock :model="items" :position="position">
    <template #itemicon="{ item }">
        <img v-tooltip.top="item.label" :alt="item.label" :src="item.icon" style="width: 100%" />
    </template>
</Dock>


```

## Advanced [#](https://primevue.org/dock/#advance)

A mock desktop UI implemented with various components in addition to Dock.

* Finder
* File

  + New

    - Bookmark
    - Video
  + Delete
  + Export
* Edit

  + Left
  + Right
  + Center
  + Justify
* Users

  + New
  + Delete
  + Search

    - Filter

      * Print
    - List
* Events

  + Edit

    - Save
    - Delete
  + Archive

    - Remove
* Quit

Fri 13:07

```

<Dock :model="items">
    <template #item="{ item }">
        <a v-tooltip.top="item.label" href="#" class="p-dock-item-link" @click="onDockItemClick($event, item)">
            <img :alt="item.label" :src="item.icon" style="width: 100%" />
        </a>
    </template>
</Dock>


```

## Accessibility [#](https://primevue.org/dock/#accessibility)

### Screen Reader

Dock component uses the *menu* role with the *aria-orientation* and the value to describe the menu can either be provided with *aria-labelledby* or *aria-label* props. Each list item has a *menuitem* role with *aria-label* referring to the label of the item and *aria-disabled* defined if the item is disabled.

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the first menuitem. |
| *enter* | Activates the focused menuitem. |
| *space* | Activates the focused menuitem. |
| *down arrow* | Moves focus to the next menuitem in vertical layout. |
| *up arrow* | Moves focus to the previous menuitem in vertical layout. |
| *right arrow* | Moves focus to the next menuitem in horizontal layout. |
| *left arrow* | Moves focus to the previous menuitem in horizontal layout. |
| *home* | Moves focus to the first menuitem. |
| *end* | Moves focus to the last menuitem. |