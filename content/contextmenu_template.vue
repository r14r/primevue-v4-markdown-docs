<ul class="m-0 p-0 list-none border border-surface-200 dark:border-surface-700 rounded p-4 flex flex-col gap-2 w-full md:w-[30rem]">
    <li
        v-for="product in products"
        :key="product.id"
        :class="['p-2 hover:bg-surface-100 dark:hover:bg-surface-800 rounded border border-transparent transition-all transition-duration-200', { 'border-primary': selectedId === product.id }]"
        @contextmenu="onRightClick($event, product.id)"
    >
        <div class="flex flex-wrap p-2 items-center gap-4">
            <img class="w-16 shrink-0 rounded" :src="'/images/product/' + product.image" :alt="product.name" />
            <div class="flex-1 flex flex-col gap-1">
                <span class="font-bold">{{ product.name }}</span>
                <div class="flex items-center gap-2">
                    <i class="pi pi-tag text-sm"></i>
                    <span>{{ product.category }}</span>
                </div>
            </div>
            <span class="font-bold ml-8">${{ product.price }}</span>
        </div>
    </li>
</ul>
<ContextMenu ref="menu" :model="items" @hide="selectedId = null">
    <template #item="{ item, props }">
        <a v-ripple class="flex items-center" v-bind="props.action">
            <span :class="item.icon" />
            <span class="ml-2">{{ item.label }}</span>
            <Badge v-if="item.badge" class="ml-auto" :value="item.badge" />
            <span v-if="item.shortcut" class="ml-auto border border-surface rounded bg-emphasis text-muted-color text-xs p-1">{{ item.shortcut }}</span>
            <i v-if="item.items" class="pi pi-angle-right ml-auto"></i>
        </a>
    </template>
</ContextMenu>