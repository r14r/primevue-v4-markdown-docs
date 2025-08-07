<Accordion value="0">
    <AccordionPanel v-for="tab in tabs" :key="tab.title" :value="tab.value">
        <AccordionHeader>{{ tab.title }}</AccordionHeader>
        <AccordionContent>
            <p class="m-0">{{ tab.content }}</p>
        </AccordionContent>
    </AccordionPanel>
</Accordion>