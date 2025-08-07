# Icons

[PrimeIcons](https://github.com/primefaces/primeicons)  is the default icon library of PrimeVue with over 250 open source icons developed by PrimeTek. PrimeIcons library is optional as PrimeVue components can use any icon with templating.

## Download [#](https://primevue.org/icons/#download)

PrimeIcons is available at npm, run the following command to download it to your project.

```

npm install primeicons


```

## Import [#](https://primevue.org/icons/#import)

CSS file of the icon library needs to be imported in *styles.scss* of your application.

```

import 'primeicons/primeicons.css'


```

## Figma [#](https://primevue.org/icons/#figma)

PrimeIcons library is now available on [Figma Community](https://www.figma.com/community/file/1354343849355792252/primeicons). By adding them as a library, you can easily use these icons in your designs.

## Basic [#](https://primevue.org/icons/#basic)

PrimeIcons use the *pi pi-{icon}* syntax such as *pi pi-check*. A standalone icon can be displayed using an element such as *i* or *span*

```

<i class="pi pi-check"></i>
<i class="pi pi-times"></i>
<span class="pi pi-search"></span>
<span class="pi pi-user"></span>


```

## Size [#](https://primevue.org/icons/#size)

Size of an icon is controlled with the font-size property of the element.

```

<i class="pi pi-check" style="font-size: 1rem"></i>
<i class="pi pi-times" style="font-size: 1.5rem"></i>
<i class="pi pi-search" style="font-size: 2rem"></i>
<i class="pi pi-user" style="font-size: 2.5rem"></i>


```

## Color [#](https://primevue.org/icons/#color)

Icon color is defined with the *color* property which is inherited from parent by default.

```

<i class="pi pi-check" style="color: slateblue"></i>
<i class="pi pi-times" style="color: green"></i>
<i class="pi pi-search" style="color: 'var(--p-primary-color)'"></i>
<i class="pi pi-user" style="color: #708090"></i>


```

## Spin [#](https://primevue.org/icons/#spin)

Special *pi-spin* class applies infinite rotation to an icon.

```

<i class="pi pi-spin pi-spinner" style="font-size: 2rem"></i>
<i class="pi pi-spin pi-cog" style="font-size: 2rem"></i>


```

## Constants [#](https://primevue.org/icons/#constants)

Constants API is available to reference icons easily when used programmatically.

* File
* New
* Open

```

<template>
    <div class="card flex justify-center">
        <Menu :model="items" />
    </div>
</template>

<script>
import { PrimeIcons } from '@primevue/core/api';

export default {
    data() {
        return {
            items: [
                {
                    label: 'File',
                    items: [
                        { label: 'New', icon: PrimeIcons.PLUS },
                        { label: 'Open', icon: PrimeIcons.DOWNLOAD }
                    ]
                }
            ]
        };
    }
};
</script>


```

## List [#](https://primevue.org/icons/#list)

Here is the full list of PrimeIcons. More icons will be added periodically and you may also [request new icons](https://github.com/primefaces/primeicons/issues) at the issue tracker.