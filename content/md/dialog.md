# Dialog

Dialog is a container to display content in an overlay window.

## Import [#](https://primevue.org/dialog/#import)

```

import Dialog from 'primevue/dialog';


```

## Basic [#](https://primevue.org/dialog/#basic)

Dialog is used as a container and visibility is controlled with a binding to *visible* property.

Show

```

<Button label="Show" @click="visible = true" />

<Dialog v-model:visible="visible" modal header="Edit Profile" :style="{ width: '25rem' }">
    <span class="text-surface-500 dark:text-surface-400 block mb-8">Update your information.</span>
    <div class="flex items-center gap-4 mb-4">
        <label for="username" class="font-semibold w-24">Username</label>
        <InputText id="username" class="flex-auto" autocomplete="off" />
    </div>
    <div class="flex items-center gap-4 mb-8">
        <label for="email" class="font-semibold w-24">Email</label>
        <InputText id="email" class="flex-auto" autocomplete="off" />
    </div>
    <div class="flex justify-end gap-2">
        <Button type="button" label="Cancel" severity="secondary" @click="visible = false"></Button>
        <Button type="button" label="Save" @click="visible = false"></Button>
    </div>
</Dialog>


```

## Template [#](https://primevue.org/dialog/#template)

Header and Footer sections allow customization via templating.

Show

```

<Button label="Show" @click="visible = true" />

<Dialog v-model:visible="visible" modal header="Edit Profile" :style="{ width: '25rem' }">
    <template #header>
        <div class="inline-flex items-center justify-center gap-2">
            <Avatar image="https://primefaces.org/cdn/primevue/images/avatar/amyelsner.png" shape="circle" />
            <span class="font-bold whitespace-nowrap">Amy Elsner</span>
        </div>
    </template>
    <span class="text-surface-500 dark:text-surface-400 block mb-8">Update your information.</span>
    <div class="flex items-center gap-4 mb-4">
        <label for="username" class="font-semibold w-24">Username</label>
        <InputText id="username" class="flex-auto" autocomplete="off" />
    </div>
    <div class="flex items-center gap-4 mb-2">
        <label for="email" class="font-semibold w-24">Email</label>
        <InputText id="email" class="flex-auto" autocomplete="off" />
    </div>
    <template #footer>
        <Button label="Cancel" text severity="secondary" @click="visible = false" autofocus />
        <Button label="Save" variant="outlined" severity="secondary" @click="visible = false" autofocus />
    </template>
</Dialog>


```

## Position [#](https://primevue.org/dialog/#position)

The *position* property defines the location of relative to the screen.

LeftRight

TopLeftTopTopRight

BottomLeftBottomBottomRight

```

<div class="flex flex-wrap justify-center gap-2 mb-2">
    <Button label="Left" icon="pi pi-arrow-right" @click="openPosition('left')" severity="secondary" style="min-width: 10rem" />
    <Button label="Right" icon="pi pi-arrow-left" @click="openPosition('right')" severity="secondary" style="min-width: 10rem" />
</div>
<div class="flex flex-wrap justify-center gap-2 mb-2">
    <Button label="TopLeft" icon="pi pi-arrow-down-right" @click="openPosition('topleft')" severity="secondary" style="min-width: 10rem" />
    <Button label="Top" icon="pi pi-arrow-down" @click="openPosition('top')" severity="secondary" style="min-width: 10rem" />
    <Button label="TopRight" icon="pi pi-arrow-down-left" @click="openPosition('topright')" severity="secondary" style="min-width: 10rem" />
</div>
<div class="flex flex-wrap justify-center gap-2">
    <Button label="BottomLeft" icon="pi pi-arrow-up-right" @click="openPosition('bottomleft')" severity="secondary" style="min-width: 10rem" />
    <Button label="Bottom" icon="pi pi-arrow-up" @click="openPosition('bottom')" severity="secondary" style="min-width: 10rem" />
    <Button label="BottomRight" icon="pi pi-arrow-up-left" @click="openPosition('bottomright')" severity="secondary" style="min-width: 10rem" />
</div>

<Dialog v-model:visible="visible" header="Edit Profile" :style="{ width: '25rem' }" :position="position" :modal="true" :draggable="false">
    <span class="text-surface-500 dark:text-surface-400 block mb-8">Update your information.</span>
    <div class="flex items-center gap-4 mb-4">
        <label for="username" class="font-semibold w-24">Username</label>
        <InputText id="username" class="flex-auto" autocomplete="off" />
    </div>
    <div class="flex items-center gap-4 mb-8">
        <label for="email" class="font-semibold w-24">Email</label>
        <InputText id="email" class="flex-auto" autocomplete="off" />
    </div>
    <div class="flex justify-end gap-2">
        <Button type="button" label="Cancel" severity="secondary" @click="visible = false"></Button>
        <Button type="button" label="Save" @click="visible = false"></Button>
    </div>
</Dialog>


```

## Maximizable [#](https://primevue.org/dialog/#maximizable)

Adding *maximizable* property enables the full screen mode.

Show

```

<Button label="Show" @click="visible = true" />

<Dialog v-model:visible="visible" maximizable modal header="Header" :style="{ width: '50rem' }" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
    <p class="m-0">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </p>
</Dialog>


```

## Long Content [#](https://primevue.org/dialog/#longcontent)

When content exceeds viewport, Dialog automatically becomes scrollable.

Show

```

<Button label="Show" @click="visible = true" />

<Dialog v-model:visible="visible" modal header="Header" :style="{ width: '50rem' }" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
    <p class="mb-8">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </p>
    <p class="mb-8">
        "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim
        ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur,
        adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid
        ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
    </p>
    <p class="mb-8">
        At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa
        qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod
        maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae
        non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.
    </p>
    <p class="mb-8">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </p>
    <p class="mb-8">
        "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim
        ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur,
        adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid
        ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
    </p>
    <p>
        At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa
        qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod
        maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae
        non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.
    </p>
</Dialog>


```

## Without Modal [#](https://primevue.org/dialog/#modal)

Mask layer behind the Dialog is configured with the *modal* property. By default, no modal layer is added.

Show

```

<Button label="Show" @click="visible = true" />

<Dialog v-model:visible="visible" header="Edit Profile" :style="{ width: '25rem' }">
    <span class="text-surface-500 dark:text-surface-400 block mb-8">Update your information.</span>
    <div class="flex items-center gap-4 mb-4">
        <label for="username" class="font-semibold w-24">Username</label>
        <InputText id="username" class="flex-auto" autocomplete="off" />
    </div>
    <div class="flex items-center gap-4 mb-8">
        <label for="email" class="font-semibold w-24">Email</label>
        <InputText id="email" class="flex-auto" autocomplete="off" />
    </div>
    <div class="flex justify-end gap-2">
        <Button type="button" label="Cancel" severity="secondary" @click="visible = false"></Button>
        <Button type="button" label="Save" @click="visible = false"></Button>
    </div>
</Dialog>


```

## Responsive [#](https://primevue.org/dialog/#responsive)

Dialog width can be adjusted per screen size with the *breakpoints* option where the max-width for the breakpoint and the width are defined as key-value pairs. When no breakpoint matches width defined in *style* or *class* is used. Alternatively responsive utility classes of libraries like Tailwind can also be used such as *md:w-screen*.

Show

```

<Button label="Show" @click="visible = true" />

<Dialog v-model:visible="visible" modal header="Header" :style="{ width: '50vw' }" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
    <p class="m-0">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </p>
</Dialog>


```

## Headless [#](https://primevue.org/dialog/#headless)

Headless mode is enabled by defining a *container* slot that lets you implement entire UI instead of the default elements.

Login

```

<Button label="Login" icon="pi pi-user" @click="visible = true" />

<Dialog v-model:visible="visible" pt:root:class="!border-0 !bg-transparent" pt:mask:class="backdrop-blur-sm">
    <template #container="{ closeCallback }">
        <div class="flex flex-col px-8 py-8 gap-6 rounded-2xl" style="background-image: radial-gradient(circle at left top, var(--p-primary-400), var(--p-primary-700))">
            <svg width="35" height="40" viewBox="0 0 35 40" fill="none" xmlns="http://www.w3.org/2000/svg" class="block mx-auto">
                <path
                    d="M25.87 18.05L23.16 17.45L25.27 20.46V29.78L32.49 23.76V13.53L29.18 14.73L25.87 18.04V18.05ZM25.27 35.49L29.18 31.58V27.67L25.27 30.98V35.49ZM20.16 17.14H20.03H20.17H20.16ZM30.1 5.19L34.89 4.81L33.08 12.33L24.1 15.67L30.08 5.2L30.1 5.19ZM5.72 14.74L2.41 13.54V23.77L9.63 29.79V20.47L11.74 17.46L9.03 18.06L5.72 14.75V14.74ZM9.63 30.98L5.72 27.67V31.58L9.63 35.49V30.98ZM4.8 5.2L10.78 15.67L1.81 12.33L0 4.81L4.79 5.19L4.8 5.2ZM24.37 21.05V34.59L22.56 37.29L20.46 39.4H14.44L12.34 37.29L10.53 34.59V21.05L12.42 18.23L17.45 26.8L22.48 18.23L24.37 21.05ZM22.85 0L22.57 0.69L17.45 13.08L12.33 0.69L12.05 0H22.85Z"
                    fill="var(--p-primary-700)"
                />
                <path
                    d="M30.69 4.21L24.37 4.81L22.57 0.69L22.86 0H26.48L30.69 4.21ZM23.75 5.67L22.66 3.08L18.05 14.24V17.14H19.7H20.03H20.16H20.2L24.1 15.7L30.11 5.19L23.75 5.67ZM4.21002 4.21L10.53 4.81L12.33 0.69L12.05 0H8.43002L4.22002 4.21H4.21002ZM21.9 17.4L20.6 18.2H14.3L13 17.4L12.4 18.2L12.42 18.23L17.45 26.8L22.48 18.23L22.5 18.2L21.9 17.4ZM4.79002 5.19L10.8 15.7L14.7 17.14H14.74H15.2H16.85V14.24L12.24 3.09L11.15 5.68L4.79002 5.2V5.19Z"
                    fill="var(--p-primary-200)"
                />
            </svg>
            <div class="inline-flex flex-col gap-2">
                <label for="username" class="text-primary-50 font-semibold">Username</label>
                <InputText id="username" class="!bg-white/20 !border-0 !p-4 !text-primary-50 w-80"></InputText>
            </div>
            <div class="inline-flex flex-col gap-2">
                <label for="password" class="text-primary-50 font-semibold">Password</label>
                <InputText id="password" class="!bg-white/20 !border-0 !p-4 !text-primary-50 w-80" type="password"></InputText>
            </div>
            <div class="flex items-center gap-4">
                <Button label="Cancel" @click="closeCallback" variant="text" class="!p-4 w-full !text-primary-50 !border !border-white/30 hover:!bg-white/10"></Button>
                <Button label="Sign-In" @click="closeCallback" variant="text" class="!p-4 w-full !text-primary-50 !border !border-white/30 hover:!bg-white/10"></Button>
            </div>
        </div>
    </template>
</Dialog>


```

## Accessibility [#](https://primevue.org/dialog/#accessibility)

### Screen Reader

Dialog component uses *dialog* role along with *aria-labelledby* referring to the header element however any attribute is passed to the root element so you may use *aria-labelledby* to override this default behavior. In addition *aria-modal* is added since focus is kept within the popup.

Trigger element also requires *aria-expanded* and *aria-controls* to be handled explicitly.

Close element is a *button* with an *aria-label* that refers to the *aria.close* property of the [locale](https://primevue.org/configuration/#locale) API by default, you may use *closeButtonProps* to customize the element and override the default *aria-label*.

```

<Button label="Show" icon="pi pi-external-link" @click="visible = true" :aria-controls="visible ? 'dlg' : null" :aria-expanded="visible ? true : false" />

<Dialog id="dlg" header="Header" v-model:visible="visible" :style="{ width: '50vw' }">
    <p>Content</p>
</Dialog>


```

### Overlay Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the next the focusable element within the dialog if *modal* is true. Otherwise, the focusable element in the page tab sequence. |
| *shift* + *tab* | Moves focus to the previous the focusable element within the dialog if *modal* is true. Otherwise, the focusable element in the page tab sequence. |
| *escape* | Closes the dialog if *closeOnEscape* is true. |

### Close Button Keyboard Support

| Key | Function |
| --- | --- |
| *enter* | Closes the dialog. |
| *space* | Closes the dialog. |