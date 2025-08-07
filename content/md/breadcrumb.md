# Breadcrumb

Breadcrumb provides contextual information about page hierarchy.

## Import [#](https://primevue.org/breadcrumb/#import)

```

import Breadcrumb from 'primevue/breadcrumb';


```

## Basic [#](https://primevue.org/breadcrumb/#basic)

Breadcrumb requires a collection of menuitems as its *model*, the root item is defined with the *home* property.

3. [Electronics](#)
5. [Computer](#)
7. [Accessories](#)
9. [Keyboard](#)
11. [Wireless](#)

```

<Breadcrumb :home="home" :model="items" />


```

## Template [#](https://primevue.org/breadcrumb/#template)

Custom content can be placed inside the items using the *item* template. The divider between the items has its own *separator* template.

2. /
4. /
6. /
8. /
10. /

```

<Breadcrumb :home="home" :model="items">
    <template #item="{ item }">
        <a class="cursor-pointer" :href="item.url">
            <span :class="item.icon"></span>
        </a>
    </template>
    <template #separator> / </template>
</Breadcrumb>


```

## Router [#](https://primevue.org/breadcrumb/#router)

Items with navigation are defined with templating to be able to use a router link component, an external link or programmatic navigation.

3. Components
5. Form
7. [InputText](https://primevue.org/inputtext)

```

<Breadcrumb :home="home" :model="items">
    <template #item="{ item, props }">
        <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
            <a :href="href" v-bind="props.action" @click="navigate">
                <span :class="[item.icon, 'text-color']" />
                <span class="text-primary font-semibold">{{ item.label }}</span>
            </a>
        </router-link>
        <a v-else :href="item.url" :target="item.target" v-bind="props.action">
            <span class="text-surface-700 dark:text-surface-0">{{ item.label }}</span>
        </a>
    </template>
</Breadcrumb>


```

## Accessibility [#](https://primevue.org/breadcrumb/#accessibility)

### Screen Reader

Breadcrumb uses the *nav* element and since any attribute is passed to the root implicitly *aria-labelledby* or *aria-label* can be used to describe the component. Inside an ordered list is used where the list item separators have *aria-hidden* to be able to ignored by the screen readers. If the last link represents the current route, *aria-current* is added with "page" as the value.

### Keyboard Support

No special keyboard interaction is needed, all menuitems are focusable based on the page tab sequence.