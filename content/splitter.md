# Splitter

Splitter is utilized to separate and resize panels.

## Import [#](https://primevue.org/splitter/#import)

```

import Splitter from 'primevue/splitter';
import SplitterPanel from 'primevue/splitterpanel';


```

## Horizontal [#](https://primevue.org/splitter/#horizontal)

Splitter requires two SplitterPanel components as children which are displayed horizontally by default.

Panel 1

Panel 2

```

<Splitter style="height: 300px">
    <SplitterPanel class="flex items-center justify-center"> Panel 1 </SplitterPanel>
    <SplitterPanel class="flex items-center justify-center"> Panel 2 </SplitterPanel>
</Splitter>


```

## Size [#](https://primevue.org/splitter/#size)

Initial dimension of a panel is percentage based and defined using the *size* property. In addition,*minSize* is provided to set a minimum value during a resize.

Panel 1

Panel 2

```

<Splitter style="height: 300px">
    <SplitterPanel class="flex items-center justify-center" :size="25" :minSize="10"> Panel 1 </SplitterPanel>
    <SplitterPanel class="flex items-center justify-center" :size="75"> Panel 2 </SplitterPanel>
</Splitter>


```

## Vertical [#](https://primevue.org/splitter/#vertical)

Panels are displayed as stacked by setting the *layout* to *vertical*.

Panel 1

Panel 2

```

<Splitter style="height: 300px" layout="vertical">
    <SplitterPanel class="flex items-center justify-center"> Panel 1 </SplitterPanel>
    <SplitterPanel class="flex items-center justify-center"> Panel 2 </SplitterPanel>
</Splitter>


```

## Nested [#](https://primevue.org/splitter/#nested)

Splitters can be combined to create advanced layouts.

Panel 1

Panel 2

Panel 3

Panel 4

```

<Splitter style="height: 300px">
    <SplitterPanel class="flex items-center justify-center" :size="20" :minSize="10"> Panel 1 </SplitterPanel>
    <SplitterPanel :size="80">
        <Splitter layout="vertical">
            <SplitterPanel class="flex items-center justify-center" :size="15"> Panel 2 </SplitterPanel>
            <SplitterPanel :size="85">
                <Splitter>
                    <SplitterPanel class="flex items-center justify-center" :size="20"> Panel 3 </SplitterPanel>
                    <SplitterPanel class="flex items-center justify-center" :size="80"> Panel 4 </SplitterPanel>
                </Splitter>
            </SplitterPanel>
        </Splitter>
    </SplitterPanel>
</Splitter>


```

## Accessibility [#](https://primevue.org/splitter/#accessibility)

### Screen Reader

Splitter bar defines *separator* as the role with *aria-orientation* set to either horizontal or vertical.

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus through the splitter bar. |
| *down arrow* | Moves a vertical splitter down. |
| *up arrow* | Moves a vertical splitter up. |
| *left arrow* | Moves a horizontal splitter to the left. |
| *right arrow* | Moves a horizontal splitter to the right. |