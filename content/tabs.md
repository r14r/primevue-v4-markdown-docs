# Tabs

Tabs facilitates seamless switching between different views.

## Import [#](https://primevue.org/tabs/#import)

```

import Tabs from 'primevue/tabs';
import TabList from 'primevue/tablist';
import Tab from 'primevue/tab';
import TabPanels from 'primevue/tabpanels';
import TabPanel from 'primevue/tabpanel';


```

## Basic [#](https://primevue.org/tabs/#basic)

Tabs is defined using *TabList*, *Tab*, *TabPanels* and *TabPanel* components. Tab and TabPanel components are associated with their *value* properties.

Header IHeader IIHeader III

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Consectetur, adipisci velit, sed quia non numquam eius modi.

At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus.

```

<Tabs value="0">
    <TabList>
        <Tab value="0">Header I</Tab>
        <Tab value="1">Header II</Tab>
        <Tab value="2">Header III</Tab>
    </TabList>
    <TabPanels>
        <TabPanel value="0">
            <p class="m-0">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
                consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            </p>
        </TabPanel>
        <TabPanel value="1">
            <p class="m-0">
                Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim
                ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Consectetur, adipisci velit, sed quia non numquam eius modi.
            </p>
        </TabPanel>
        <TabPanel value="2">
            <p class="m-0">
                At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa
                qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus.
            </p>
        </TabPanel>
    </TabPanels>
</Tabs>


```

## Dynamic [#](https://primevue.org/tabs/#dynamic)

Tabs can be generated dynamically using the standard *v-for* directive on Tab and TabPanel.

Tab 1Tab 2Tab 3

Tab 1 Content

Tab 2 Content

Tab 3 Content

```

<Tabs value="0">
    <TabList>
        <Tab v-for="tab in tabs" :key="tab.title" :value="tab.value">{{ tab.title }}</Tab>
    </TabList>
    <TabPanels>
        <TabPanel v-for="tab in tabs" :key="tab.content" :value="tab.value">
            <p class="m-0">{{ tab.content }}</p>
        </TabPanel>
    </TabPanels>
</Tabs>


```

## Controlled [#](https://primevue.org/tabs/#controlled)

Tabs can be controlled programmatically using *value* property as a model.

123

Header IHeader IIHeader III

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Consectetur, adipisci velit, sed quia non numquam eius modi.

At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus.

```

<div class="flex mb-2 gap-2 justify-end">
    <Button @click="value = '0'" rounded label="1" class="w-8 h-8 p-0" :outlined="value !== '0'" />
    <Button @click="value = '1'" rounded label="2" class="w-8 h-8 p-0" :outlined="value !== '1'" />
    <Button @click="value = '2'" rounded label="3" class="w-8 h-8 p-0" :outlined="value !== '2'" />
</div>

<Tabs v-model:value="value">
    <TabList>
        <Tab value="0">Header I</Tab>
        <Tab value="1">Header II</Tab>
        <Tab value="2">Header III</Tab>
    </TabList>
    <TabPanels>
        <TabPanel value="0">
            <p class="m-0">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
                consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            </p>
        </TabPanel>
        <TabPanel value="1">
            <p class="m-0">
                Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim
                ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Consectetur, adipisci velit, sed quia non numquam eius modi.
            </p>
        </TabPanel>
        <TabPanel value="2">
            <p class="m-0">
                At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa
                qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus.
            </p>
        </TabPanel>
    </TabPanels>
</Tabs>


```

## Scrollable [#](https://primevue.org/tabs/#scrollable)

Adding *scrollable* property displays navigational buttons at each side to scroll between tabs.

Tab 1Tab 2Tab 3Tab 4Tab 5Tab 6Tab 7Tab 8Tab 9Tab 10Tab 11Tab 12Tab 13Tab 14Tab 15Tab 16Tab 17Tab 18Tab 19Tab 20Tab 21Tab 22Tab 23Tab 24Tab 25Tab 26Tab 27Tab 28Tab 29Tab 30Tab 31Tab 32Tab 33Tab 34Tab 35Tab 36Tab 37Tab 38Tab 39Tab 40Tab 41Tab 42Tab 43Tab 44Tab 45Tab 46Tab 47Tab 48Tab 49Tab 50

Tab 1 Content

Tab 2 Content

Tab 3 Content

Tab 4 Content

Tab 5 Content

Tab 6 Content

Tab 7 Content

Tab 8 Content

Tab 9 Content

Tab 10 Content

Tab 11 Content

Tab 12 Content

Tab 13 Content

Tab 14 Content

Tab 15 Content

Tab 16 Content

Tab 17 Content

Tab 18 Content

Tab 19 Content

Tab 20 Content

Tab 21 Content

Tab 22 Content

Tab 23 Content

Tab 24 Content

Tab 25 Content

Tab 26 Content

Tab 27 Content

Tab 28 Content

Tab 29 Content

Tab 30 Content

Tab 31 Content

Tab 32 Content

Tab 33 Content

Tab 34 Content

Tab 35 Content

Tab 36 Content

Tab 37 Content

Tab 38 Content

Tab 39 Content

Tab 40 Content

Tab 41 Content

Tab 42 Content

Tab 43 Content

Tab 44 Content

Tab 45 Content

Tab 46 Content

Tab 47 Content

Tab 48 Content

Tab 49 Content

Tab 50 Content

```

<Tabs value="0" scrollable>
    <TabList>
        <Tab v-for="tab in scrollableTabs" :key="tab.title" :value="tab.value">
            {{ tab.title }}
        </Tab>
    </TabList>
    <TabPanels>
        <TabPanel v-for="tab in scrollableTabs" :key="tab.content" :value="tab.value">
            <p class="m-0">{{ tab.content }}</p>
        </TabPanel>
    </TabPanels>
</Tabs>


```

## Disabled [#](https://primevue.org/tabs/#disabled)

Enabling *disabled* property of a Tab prevents user interaction.

Header IHeader IIHeader IIIHeader IV

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Consectetur, adipisci velit, sed quia non numquam eius modi.

At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus.

```

<Tabs value="0">
    <TabList>
        <Tab value="0">Header I</Tab>
        <Tab value="1">Header II</Tab>
        <Tab value="2">Header III</Tab>
        <Tab disabled>Header IV</Tab>
    </TabList>
    <TabPanels>
        <TabPanel value="0">
            <p class="m-0">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
                consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            </p>
        </TabPanel>
        <TabPanel value="1">
            <p class="m-0">
                Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim
                ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Consectetur, adipisci velit, sed quia non numquam eius modi.
            </p>
        </TabPanel>
        <TabPanel value="2">
            <p class="m-0">
                At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa
                qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus.
            </p>
        </TabPanel>
    </TabPanels>
</Tabs>


```

## Template [#](https://primevue.org/tabs/#template)

Custom content for a tab is defined with the default slot. The optional *as* property controls the default container element of a tab, for example setting it to a *div* renders a div for the header instead of a button. The *asChild* option enables the headless mode for further customization by passing callbacks and properties to implement your own tab header.

Amy Elsner

Onyama Limba

Ioni Bowcher2

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Consectetur, adipisci velit, sed quia non numquam eius modi.

At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus.

```

<Tabs value="0">
    <TabList>
        <Tab value="0" as="div" class="flex items-center gap-2">
            <Avatar image="https://primefaces.org/cdn/primevue/images/avatar/amyelsner.png" shape="circle" />
            <span class="font-bold whitespace-nowrap">Amy Elsner</span>
        </Tab>
        <Tab value="1" as="div" class="flex items-center gap-2">
            <Avatar image="https://primefaces.org/cdn/primevue/images/avatar/onyamalimba.png" shape="circle" />
            <span class="font-bold whitespace-nowrap">Onyama Limba</span>
        </Tab>
        <Tab v-slot="slotProps" value="2" asChild>
            <div :class="['flex items-center gap-2', slotProps.class]" @click="slotProps.onClick" v-bind="slotProps.a11yAttrs">
                <Avatar image="https://primefaces.org/cdn/primevue/images/avatar/ionibowcher.png" shape="circle" />
                <span class="font-bold whitespace-nowrap">Ioni Bowcher</span>
                <Badge value="2" />
            </div>
        </Tab>
    </TabList>
    <TabPanels>
        <TabPanel value="0" as="p" class="m-0">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </TabPanel>
        <TabPanel value="1" as="p" class="m-0">
            Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim
            ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Consectetur, adipisci velit, sed quia non numquam eius modi.
        </TabPanel>
        <TabPanel v-slot="slotProps" value="2" asChild>
            <div v-show="slotProps.active" :class="slotProps.class" v-bind="slotProps.a11yAttrs">
                <p class="m-0">
                    At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in
                    culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus.
                </p>
            </div>
        </TabPanel>
    </TabPanels>
</Tabs>


```

## Tab Menu [#](https://primevue.org/tabs/#tabmenu)

A navigation menu is implemented using tabs without the panels where the content of a tab is provided by a route component like [router-view](https://router.vuejs.org/guide/essentials/nested-routes#Nested-Named-Routes). For the purpose of this demo, *router-view* is not included.

Dashboard

Transactions

Products

Messages

```

<Tabs value="/dashboard">
    <TabList>
        <Tab v-for="tab in items" :key="tab.label" :value="tab.route">
            <router-link v-if="tab.route" v-slot="{ href, navigate }" :to="tab.route" custom>
                <a v-ripple :href="href" @click="navigate" class="flex items-center gap-2 text-inherit">
                    <i :class="tab.icon" />
                    <span>{{ tab.label }}</span>
                </a>
            </router-link>
        </Tab>
    </TabList>
</Tabs>


```

## Accessibility [#](https://primevue.org/tabs/#accessibility)

### Screen Reader

The tabs container in TabList is defined with the *tablist* role, as any attribute is passed to the container element *aria-labelledby* can be optionally used to specify an element to describe the Tabs. Each Tab has a *tab* role along with *aria-selected* state attribute and *aria-controls* to refer to the corresponding TabPanel. TabPanel has *tabpanel* role, an id to match the *aria-controls* of Tab and *aria-labelledby* reference to Tab as the accessible name.

### Tab Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus through the header. |
| *enter* | Activates the focused tab header. |
| *space* | Activates the focused tab header. |
| *right arrow* | Moves focus to the next header. If focus is on the last header, moves focus to the first header. |
| *left arrow* | Moves focus to the previous header. If focus is on the first header, moves focus to the last header. |
| *home* | Moves focus to the last header. |
| *end* | Moves focus to the first header. |
| *pageUp* | Moves scroll position to first header. |
| *pageDown* | Moves scroll position to last header. |