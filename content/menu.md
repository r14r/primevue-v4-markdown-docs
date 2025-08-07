# Menu

Menu displays a list of items in vertical orientation.

## Import [#](https://primevue.org/menu/#import)

```

import Menu from 'primevue/menu';


```

## Basic [#](https://primevue.org/menu/#basic)

Menu requires a collection of menuitems as its *model*.

* New
* Search

```

<Menu :model="items" />


```

## Group [#](https://primevue.org/menu/#group)

Menu supports single level of grouping by defining children with the *items* property.

* Documents
* New
* Search
* Profile
* Settings
* Logout

```

<Menu :model="items" />


```

## Popup [#](https://primevue.org/menu/#popup)

Overlay mode is enabled by adding *popup* property and calling *toggle* function of the menu ref with an event of the target.

```

<Button type="button" icon="pi pi-ellipsis-v" @click="toggle" aria-haspopup="true" aria-controls="overlay_menu" />
<Menu ref="menu" id="overlay_menu" :model="items" :popup="true" />


```

## Template [#](https://primevue.org/menu/#template)

Menu offers item customization with the *item* template that receives the menuitem instance from the model as a parameter. The submenu label has its own *submenulabel* template, additional slots named *start* and *end* are provided to embed content before or after the menu.

PRIMEAPP

* Documents
* New⌘+N
* Search⌘+S
* Profile
* Settings⌘+O
* Messages2
* Logout⌘+Q

Amy ElsnerAdmin

```

<Menu :model="items" class="w-full md:w-60">
    <template #start>
        <span class="inline-flex items-center gap-1 px-2 py-2">
            <svg width="35" height="40" viewBox="0 0 35 40" fill="none" xmlns="http://www.w3.org/2000/svg" class="h-8">
                <path d="..." fill="var(--p-primary-color)" />
                <path d="..." fill="var(--p-text-color)" />
            </svg>
            <span class="text-xl font-semibold">PRIME<span class="text-primary">APP</span></span>
        </span>
    </template>
    <template #submenulabel="{ item }">
        <span class="text-primary font-bold">{{ item.label }}</span>
    </template>
    <template #item="{ item, props }">
        <a v-ripple class="flex items-center" v-bind="props.action">
            <span :class="item.icon" />
            <span>{{ item.label }}</span>
            <Badge v-if="item.badge" class="ml-auto" :value="item.badge" />
            <span v-if="item.shortcut" class="ml-auto border border-surface rounded bg-emphasis text-muted-color text-xs p-1">{{ item.shortcut }}</span>
        </a>
    </template>
    <template #end>
        <button v-ripple class="relative overflow-hidden w-full border-0 bg-transparent flex items-start p-2 pl-4 hover:bg-surface-100 dark:hover:bg-surface-800 rounded-none cursor-pointer transition-colors duration-200">
            <Avatar image="https://primefaces.org/cdn/primevue/images/avatar/amyelsner.png" class="mr-2" shape="circle" />
            <span class="inline-flex flex-col items-start">
                <span class="font-bold">Amy Elsner</span>
                <span class="text-sm">Admin</span>
            </span>
        </button>
    </template>
</Menu>


```

## Command [#](https://primevue.org/menu/#command)

The *command* property defines the callback to run when an item is activated by click or a key event.

* New
* Search

```

<Menu :model="items" />
<Toast />


```

## Router [#](https://primevue.org/menu/#router)

Items with navigation are defined with templating to be able to use a router link component, an external link or programmatic navigation.

* Navigate
* [Router Link](https://primevue.org/theming/unstyled)
* Programmatic
* [External](https://vuejs.org/)

```

<Menu :model="items">
    <template #item="{ item, props }">
        <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
            <a v-ripple :href="href" v-bind="props.action" @click="navigate">
                <span :class="item.icon" />
                <span class="ml-2">{{ item.label }}</span>
            </a>
        </router-link>
        <a v-else v-ripple :href="item.url" :target="item.target" v-bind="props.action">
            <span :class="item.icon" />
            <span class="ml-2">{{ item.label }}</span>
        </a>
    </template>
</Menu>


```

## Accessibility [#](https://primevue.org/menu/#accessibility)

### Screen Reader

Menu component uses the *menu* role and the value to describe the menu can either be provided with *aria-labelledby* or *aria-label* props. Each list item has a *menuitem* role with *aria-label* referring to the label of the item and *aria-disabled* defined if the item is disabled.

In popup mode, the component implicitly manages the *aria-expanded*, *aria-haspopup* and *aria-controls* attributes of the target element to define the relation between the target and the popup.

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Add focus to the first item if focus moves in to the menu. If the focus is already within the menu, focus moves to the next focusable item in the page tab sequence. |
| *shift* + *tab* | Add focus to the first item if focus moves in to the menu. If the focus is already within the menu, focus moves to the previous focusable item in the page tab sequence. |
| *enter* | Activates the focused menuitem. If menu is in overlay mode, popup gets closes and focus moves to target. |
| *space* | Activates the focused menuitem. If menu is in overlay mode, popup gets closes and focus moves to target. |
| *escape* | If menu is in overlay mode, popup gets closes and focus moves to target. |
| *down arrow* | Moves focus to the next menuitem. |
| *up arrow* | Moves focus to the previous menuitem. |
| *alt* + *up arrow* | If menu is in overlay mode, popup gets closes and focus moves to the target. |
| *home* | Moves focus to the first menuitem. |
| *end* | Moves focus to the last menuitem. |