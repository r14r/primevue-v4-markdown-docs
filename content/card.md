# Card

Card is a flexible container component.

## Import [#](https://primevue.org/card/#import)

```

import Card from 'primevue/card';


```

## Basic [#](https://primevue.org/card/#basic)

A simple Card is created with a *title* property along with the content as children.

Simple Card

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!

```

<Card>
    <template #title>Simple Card</template>
    <template #content>
        <p class="m-0">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque
            quas!
        </p>
    </template>
</Card>


```

## Advanced [#](https://primevue.org/card/#advanced)

Card provides *header*, *title*, *subtitle*, *content* and *footer* as the named templates to place content.

Advanced Card

Card subtitle

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!

CancelSave

```

<Card style="width: 25rem; overflow: hidden">
    <template #header>
        <img alt="user header" src="/images/usercard.png" />
    </template>
    <template #title>Advanced Card</template>
    <template #subtitle>Card subtitle</template>
    <template #content>
        <p class="m-0">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque
            quas!
        </p>
    </template>
    <template #footer>
        <div class="flex gap-4 mt-1">
            <Button label="Cancel" severity="secondary" variant="outlined" class="w-full" />
            <Button label="Save" class="w-full" />
        </div>
    </template>
</Card>


```

## Accessibility [#](https://primevue.org/card/#accessibility)

### Screen Reader

A card can be utilized in many use cases as a result no role is enforced, in fact a role may not be necessary if the card is used for presentational purposes only. Any valid attribute is passed to the container element so if you require to use one of the [landmark](https://www.w3.org/TR/wai-aria/#landmark) roles like *region*, you may use the *role* property.

```

<Card role="region">
    Content
</Card>


```

### Keyboard Support

Component does not include any interactive elements.