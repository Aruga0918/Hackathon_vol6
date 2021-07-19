/* eslint-disable */
import mockServer from 'axios-mock-server'
import mock0 from './mock/users/withdrawal'
import mock1 from './mock/users/index'
import mock2 from './mock/users/edit'
import mock3 from './mock/users/_userId/index'
import mock4 from './mock/users/_userId/community'
import mock5 from './mock/shops/_shopId'
import mock6 from './mock/rankings/shops/_shopId'
import mock7 from './mock/posts/users/_userId/shops/_shopId'
import mock8 from './mock/posts/users/_userId/index'
import mock9 from './mock/posts/shops/_shopId'
import mock10 from './mock/posts/communities/_communityId'
import mock11 from './mock/posts/_postId'
import mock12 from './mock/communities/create'
import mock13 from './mock/communities/_communityId/members/_userId/index'
import mock14 from './mock/communities/_communityId/join'
import mock15 from './mock/communities/_communityId/index'
import mock16 from './mock/communities/_communityId/add'
import mock17 from './mock/categories/index'
import mock18 from './mock/categories/_categoryId/shops'

export default (client) => mockServer([
  {
    path: '/mock/users/withdrawal',
    methods: mock0
  },
  {
    path: '/mock/users',
    methods: mock1
  },
  {
    path: '/mock/users/edit',
    methods: mock2
  },
  {
    path: '/mock/users/_userId',
    methods: mock3
  },
  {
    path: '/mock/users/_userId/community',
    methods: mock4
  },
  {
    path: '/mock/shops/_shopId',
    methods: mock5
  },
  {
    path: '/mock/rankings/shops/_shopId',
    methods: mock6
  },
  {
    path: '/mock/posts/users/_userId/shops/_shopId',
    methods: mock7
  },
  {
    path: '/mock/posts/users/_userId',
    methods: mock8
  },
  {
    path: '/mock/posts/shops/_shopId',
    methods: mock9
  },
  {
    path: '/mock/posts/communities/_communityId',
    methods: mock10
  },
  {
    path: '/mock/posts/_postId',
    methods: mock11
  },
  {
    path: '/mock/communities/create',
    methods: mock12
  },
  {
    path: '/mock/communities/_communityId/members/_userId',
    methods: mock13
  },
  {
    path: '/mock/communities/_communityId/join',
    methods: mock14
  },
  {
    path: '/mock/communities/_communityId',
    methods: mock15
  },
  {
    path: '/mock/communities/_communityId/add',
    methods: mock16
  },
  {
    path: '/mock/categories',
    methods: mock17
  },
  {
    path: '/mock/categories/_categoryId/shops',
    methods: mock18
  }
], client, '')
