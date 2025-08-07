# Chip

Chip represents entities using icons, labels and images.

## Import [#](https://primevue.org/chip/#import)

```

import Chip from 'primevue/chip';


```

## Basic [#](https://primevue.org/chip/#basic)

A basic chip with a text is created with the *label* property. In addition when *removable* is added, a delete icon is displayed to remove a chip.

Action

Comedy

Mystery

Thriller

```

<Chip label="Action" />
<Chip label="Comedy" />
<Chip label="Mystery" />
<Chip label="Thriller" removable />


```

## Icon [#](https://primevue.org/chip/#icon)

A font icon next to the label can be displayed with the *icon* property.

Apple

Facebook

Google

Microsoft

GitHub

```

<Chip label="Apple" icon="pi pi-apple" />
<Chip label="Facebook" icon="pi pi-facebook" />
<Chip label="Google" icon="pi pi-google" />
<Chip label="Microsoft" icon="pi pi-microsoft" removable />
<Chip label="GitHub" icon="pi pi-github" removable>
    <template #removeicon="{ removeCallback, keydownCallback }">
        <i class="pi pi-minus-circle" @click="removeCallback" @keydown="keydownCallback" />
    </template>
</Chip>


```

## Image [#](https://primevue.org/chip/#image)

The *image* property is used to display an image like an avatar.

Amy Elsner

Asiya Javayant

Onyama Limba

Xuxue Feng

```

<Chip label="Amy Elsner" image="/images/avatar/amyelsner.png" />
<Chip label="Asiya Javayant" image="/images/avatar/asiyajavayant.png" />
<Chip label="Onyama Limba" image="/images/avatar/onyamalimba.png" />
<Chip label="Xuxue Feng" image="/images/avatar/xuxuefeng.png" removable />


```

## Template [#](https://primevue.org/chip/#templatedoc)

The default slot allows displaying custom content inside a chip.

PPRIME

```

<Chip class="py-0 pl-0 pr-4">
    <span class="bg-primary text-primary-contrast rounded-full w-8 h-8 flex items-center justify-center">P</span>
    <span class="ml-2 font-medium">PRIME</span>
</Chip>


```

## Accessibility [#](https://primevue.org/chip/#accessibility)

### Screen Reader

Chip uses the *label* property as the default *aria-label*, since any attribute is passed to the root element *aria-labelledby* or *aria-label* can be used to override the default behavior. Removable chips have a *tabindex* and focusable with the tab key.

### Keyboard Support

| Key | Function |
| --- | --- |
| *backspace* | Hides removable. |
| *enter* | Hides removable. |