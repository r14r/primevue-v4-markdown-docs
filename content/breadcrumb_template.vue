<Breadcrumb :home="home" :model="items">
    <template #item="{ item }">
        <a class="cursor-pointer" :href="item.url">
            <span :class="item.icon"></span>
        </a>
    </template>
    <template #separator> / </template>
</Breadcrumb>