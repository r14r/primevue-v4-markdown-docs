# PanelMenu

PanelMenu is a hybrid of accordion-tree components.

## Import [#](https://primevue.org/panelmenu/#import)

```

import PanelMenu from 'primevue/panelmenu';


```

## Basic [#](https://primevue.org/panelmenu/#basic)

PanelMenu requires a collection of menuitems as its *model*.

Files

* Documents

  + Invoices

    - Pending
    - Paid
  + Clients
* Images

  + Logos

Cloud

* Upload
* Download
* Sync

Devices

* Phone
* Desktop
* Tablet

```

<PanelMenu :model="items" />


```

## Multiple [#](https://primevue.org/panelmenu/#multiple)

Only one root menuitem at a time can be active by default, enabling *multiple* property changes this behavior to allow multiple root menuitems.

Files

* Documents

  + Invoices

    - Pending
    - Paid
  + Clients
* Images

  + Logos

Cloud

* Upload
* Download
* Sync

Devices

* Phone
* Desktop
* Tablet

```

<PanelMenu :model="items" multiple />


```

## Controlled [#](https://primevue.org/panelmenu/#controlled)

If the menuitem has a *key* defined, PanelMenu state can be controlled programmatically with the *expandedKeys* property that defines the keys that are expanded. This property is a Map instance whose key is the key of a node and value is a boolean.

Toggle All

Users

* New

  + Member
  + Group
* Search

Tasks

* Add New
* Pending
* Overdue

Calendar

* New Event
* Today
* This Week

```

<Button type="button" label="Toggle All" text @click="toggleAll" />
<PanelMenu v-model:expandedKeys="expandedKeys" :model="items" />


```

## Template [#](https://primevue.org/panelmenu/#template)

PanelMenu offers item customization with the *item* template that receives the menuitem instance from the model as a parameter.

Mail5

* Compose⌘+N
* Inbox5
* Sent⌘+S
* Trash⌘+T

Reports⌘+R

* Sales3
* Products6

Profile⌘+W

* Settings⌘+O
* Privacy⌘+P

```

<PanelMenu :model="items">
    <template #item="{ item }">
        <a v-ripple class="flex items-center px-4 py-2 cursor-pointer group">
            <span :class="[item.icon, 'text-primary group-hover:text-inherit']" />
            <span :class="['ml-2', { 'font-semibold': item.items }]">{{ item.label }}</span>
            <Badge v-if="item.badge" class="ml-auto" :value="item.badge" />
            <span v-if="item.shortcut" class="ml-auto border border-surface rounded bg-emphasis text-muted-color text-xs p-1">{{ item.shortcut }}</span>
        </a>
    </template>
</PanelMenu>


```

## Command [#](https://primevue.org/panelmenu/#command)

The *command* property defines the callback to run when an item is activated by click or a key event.

Files

* New
* Search
* Print

Sync

* Import
* Export

Sign Out

```

<PanelMenu :model="items" />
<Toast />


```

## Router [#](https://primevue.org/panelmenu/#router)

Items with navigation are defined with templating to be able to use a router link component, an external link or programmatic navigation.

Router

* [Styled](https://primevue.org/theming/styled)
* [Unstyled](https://primevue.org/theming/unstyled)

Programmatic

External

* [Vue.js](https://vuejs.org/)
* [Vite.js](https://vuejs.org/)

```

<PanelMenu :model="items">
    <template #item="{ item }">
        <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
            <a v-ripple class="flex items-center cursor-pointer text-surface-700 dark:text-surface-0 px-4 py-2" :href="href" @click="navigate">
                <span :class="item.icon" />
                <span class="ml-2">{{ item.label }}</span>
            </a>
        </router-link>
        <a v-else v-ripple class="flex items-center cursor-pointer text-surface-700 dark:text-surface-0 px-4 py-2" :href="item.url" :target="item.target">
            <span :class="item.icon" />
            <span class="ml-2">{{ item.label }}</span>
            <span v-if="item.items" class="pi pi-angle-down text-primary ml-auto" />
        </a>
    </template>
</PanelMenu>


```

## Accessibility [#](https://primevue.org/panelmenu/#accessibility)

### Screen Reader

Accordion header elements have a *button* role, an *aria-label* defined using the *label* property of the menuitem model and *aria-controls* to define the id of the content section along with *aria-expanded* for the visibility state.

The content of an accordion panel uses *region* role, defines an id that matches the *aria-controls* of the header and *aria-labelledby* referring to the id of the header.

The tree elements has a *tree* as the role and each menu item has a *treeitem* role along with *aria-label* and *aria-expanded* attributes. The container element of a treenode has the *group* role. The *aria-setsize*, *aria-posinset* and *aria-level* attributes are calculated implicitly and added to each treeitem.

### Header Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the next the focusable element in the page tab sequence. |
| *shift* + *tab* | Moves focus to the previous the focusable element in the page tab sequence. |
| *enter* | Toggles the visibility of the content. |
| *space* | Toggles the visibility of the content. |
| *down arrow* | Moves focus to the next header. If focus is on the last header, moves focus to the first header. |
| *up arrow* | Moves focus to the previous header. If focus is on the first header, moves focus to the last header. |
| *home* | Moves focus to the first header. |
| *end* | Moves focus to the last header. |