<ul class="m-0 list-none border border-surface rounded p-4 flex flex-col gap-2 w-full sm:w-96">
    <li
        v-for="user in users"
        :key="user.id"
        :class="['p-2 hover:bg-emphasis rounded border border-transparent transition-all duration-200 flex items-center justify-content-between', { 'border-primary': selectedUser?.id === user.id }]"
        @contextmenu="onRightClick($event, user)"
    >
        <div class="flex flex-1 items-center gap-2">
            <img :alt="user.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${user.image}`" class="w-8 h-8" />
            <span class="font-bold">{{ user.name }}</span>
        </div>
        <Tag :value="user.role" :severity="getBadge(user)" />
    </li>
</ul>
<ContextMenu ref="menu" :model="items" @hide="selectedUser = null" />
<Toast />