<Timeline :value="events" layout="horizontal" align="top">
    <template #content="slotProps">
        {{ slotProps.item }}
    </template>
</Timeline>

<Timeline :value="events" layout="horizontal" align="bottom">
    <template #content="slotProps">
        {{ slotProps.item }}
    </template>
</Timeline>

<Timeline :value="events" layout="horizontal" align="alternate">
    <template #opposite> &nbsp; </template>
    <template #content="slotProps">
        {{ slotProps.item }}
    </template>
</Timeline>