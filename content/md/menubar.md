# Menubar

Menubar also known as Navbar, is a horizontal menu component.

## Import [#](https://primevue.org/menubar/#import)

```

import Menubar from 'primevue/menubar';


```

## Basic [#](https://primevue.org/menubar/#basic)

Menubar requires a collection of menuitems as its *model*.

* Home
* Features
* Projects

  + Components
  + Blocks
  + UI Kit
  + Templates

    - Apollo
    - Ultima
* Contact

```

<Menubar :model="items" />


```

## Advanced [#](https://primevue.org/menubar/#advanced)

Menubar is a simple horizontal navigation component, for advanced use cases consider [Marketing](https://primeblocks.org/marketing/navbar) and [Application](https://primeblocks.org/application/navbar) NavBars in PrimeBlocks or [templates](https://primevue.org/templates) with horizontal menus in application templates.

## Template [#](https://primevue.org/menubar/#template)

Menubar offers item customization with the *item* template that receives the menuitem instance from the model as a parameter. Additional slots named *start* and *end* are provided to embed content before or after the menu.

* Home
* Projects3

  + Core⌘+S
  + Blocks⌘+B
  + UI Kit⌘+U

```

<Menubar :model="items">
    <template #start>
        <svg width="35" height="40" viewBox="0 0 35 40" fill="none" xmlns="http://www.w3.org/2000/svg" class="h-8">
            <path d="..." fill="var(--p-primary-color)" />
            <path d="..." fill="var(--p-text-color)" />
        </svg>
    </template>
    <template #item="{ item, props, hasSubmenu, root }">
        <a v-ripple class="flex items-center" v-bind="props.action">
            <span>{{ item.label }}</span>
            <Badge v-if="item.badge" :class="{ 'ml-auto': !root, 'ml-2': root }" :value="item.badge" />
            <span v-if="item.shortcut" class="ml-auto border border-surface rounded bg-emphasis text-muted-color text-xs p-1">{{ item.shortcut }}</span>
            <i v-if="hasSubmenu" :class="['pi pi-angle-down ml-auto', { 'pi-angle-down': root, 'pi-angle-right': !root }]"></i>
        </a>
    </template>
    <template #end>
        <div class="flex items-center gap-2">
            <InputText placeholder="Search" type="text" class="w-32 sm:w-auto" />
            <Avatar image="/images/avatar/amyelsner.png" shape="circle" />
        </div>
    </template>
</Menubar>


```

## Command [#](https://primevue.org/menubar/#command)

The *command* property defines the callback to run when an item is activated by click or a key event.

* File

  + New
  + Print
* Search
* Sync

  + Import
  + Export

```

<Menubar :model="items" />
<Toast />


```

## Router [#](https://primevue.org/menubar/#router)

Items with navigation are defined with templating to be able to use a router link component, an external link or programmatic navigation.

* Router

  + [Styled](https://primevue.org/theming/styled)
  + [Unstyled](https://primevue.org/theming/unstyled)
* Programmatic
* External

  + [Vue.js](https://vuejs.org/)
  + [Vite.js](https://vitejs.dev/)

```

<Menubar :model="items">
    <template #item="{ item, props, hasSubmenu }">
        <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
            <a v-ripple :href="href" v-bind="props.action" @click="navigate">
                <span :class="item.icon" />
                <span>{{ item.label }}</span>
            </a>
        </router-link>
        <a v-else v-ripple :href="item.url" :target="item.target" v-bind="props.action">
            <span :class="item.icon" />
            <span>{{ item.label }}</span>
            <span v-if="hasSubmenu" class="pi pi-fw pi-angle-down" />
        </a>
    </template>
</Menubar>


```

## Accessibility [#](https://primevue.org/menubar/#accessibility)

### Screen Reader

Menubar component uses the *menubar* role and the value to describe the menu can either be provided with *aria-labelledby* or *aria-label* props. Each list item has a *menuitem* role with *aria-label* referring to the label of the item and *aria-disabled* defined if the item is disabled. A submenu within a MenuBar uses the *menu* role with an *aria-labelledby* defined as the id of the submenu root menuitem label. In addition, menuitems that open a submenu have *aria-haspopup*, *aria-expanded* and *aria-controls* to define the relation between the item and the submenu.

In mobile viewports, a menu icon appears with a *button* role along with *aria-haspopup*, *aria-expanded* and *aria-controls* to manage the relation between the overlay menubar and the button. The value to describe the button can be defined *aria-label* or *aria-labelledby* specified using *buttonProps*, by default *navigation* key of the *aria* property from the [locale](https://primevue.org/configuration/#locale) API as the *aria-label*.

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Add focus to the first item if focus moves in to the menu. If the focus is already within the menu, focus moves to the next focusable item in the page tab sequence. |
| *shift* + *tab* | Add focus to the first item if focus moves in to the menu. If the focus is already within the menu, focus moves to the previous focusable item in the page tab sequence. |
| *enter* | If menuitem has a submenu, toggles the visibility of the submenu otherwise activates the menuitem and closes all open overlays. |
| *space* | If menuitem has a submenu, toggles the visibility of the submenu otherwise activates the menuitem and closes all open overlays. |
| *escape* | If focus is inside a popup submenu, closes the submenu and moves focus to the root item of the closed submenu. |
| *down arrow* | If focus is on a root element, open a submenu and moves focus to the first element in the submenu otherwise moves focus to the next menuitem within the submenu. |
| *up arrow* | If focus is on a root element, opens a submenu and moves focus to the last element in the submenu otherwise moves focus to the previous menuitem within the submenu. |
| *right arrow* | If focus is on a root element, moves focus to the next menuitem otherwise opens a submenu if there is one available and moves focus to the first item. |
| *left arrow* | If focus is on a root element, moves focus to the previous menuitem otherwise closes a submenu and moves focus to the root item of the closed submenu. |
| *home* | Moves focus to the first menuitem within the submenu. |
| *end* | Moves focus to the last menuitem within the submenu. |
| *any printable character* | Moves focus to the menuitem whose label starts with the characters being typed. |