# coding: utf-8

"""
 Copyright 2023 TikTok Pte. Ltd.

 This source code is licensed under the MIT license found in
 the LICENSE file in the root directory of this source tree.
"""
import pprint
import re  # noqa: F401

import six

class FilteringOptimizerRuleResultList(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'action': 'str',
        'data_dimension': 'str',
        'rule_info': 'list[str]',
        'status': 'str',
        'time': 'list[str]'
    }

    attribute_map = {
        'action': 'action',
        'data_dimension': 'data_dimension',
        'rule_info': 'rule_info',
        'status': 'status',
        'time': 'time'
    }

    def __init__(self, action=None, data_dimension=None, rule_info=None, status=None, time=None):  # noqa: E501
        """FilteringOptimizerRuleResultList - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._data_dimension = None
        self._rule_info = None
        self._status = None
        self._time = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if data_dimension is not None:
            self.data_dimension = data_dimension
        if rule_info is not None:
            self.rule_info = rule_info
        if status is not None:
            self.status = status
        if time is not None:
            self.time = time

    @property
    def action(self):
        """Gets the action of this FilteringOptimizerRuleResultList.  # noqa: E501


        :return: The action of this FilteringOptimizerRuleResultList.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this FilteringOptimizerRuleResultList.


        :param action: The action of this FilteringOptimizerRuleResultList.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def data_dimension(self):
        """Gets the data_dimension of this FilteringOptimizerRuleResultList.  # noqa: E501


        :return: The data_dimension of this FilteringOptimizerRuleResultList.  # noqa: E501
        :rtype: str
        """
        return self._data_dimension

    @data_dimension.setter
    def data_dimension(self, data_dimension):
        """Sets the data_dimension of this FilteringOptimizerRuleResultList.


        :param data_dimension: The data_dimension of this FilteringOptimizerRuleResultList.  # noqa: E501
        :type: str
        """

        self._data_dimension = data_dimension

    @property
    def rule_info(self):
        """Gets the rule_info of this FilteringOptimizerRuleResultList.  # noqa: E501


        :return: The rule_info of this FilteringOptimizerRuleResultList.  # noqa: E501
        :rtype: list[str]
        """
        return self._rule_info

    @rule_info.setter
    def rule_info(self, rule_info):
        """Sets the rule_info of this FilteringOptimizerRuleResultList.


        :param rule_info: The rule_info of this FilteringOptimizerRuleResultList.  # noqa: E501
        :type: list[str]
        """

        self._rule_info = rule_info

    @property
    def status(self):
        """Gets the status of this FilteringOptimizerRuleResultList.  # noqa: E501


        :return: The status of this FilteringOptimizerRuleResultList.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FilteringOptimizerRuleResultList.


        :param status: The status of this FilteringOptimizerRuleResultList.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def time(self):
        """Gets the time of this FilteringOptimizerRuleResultList.  # noqa: E501


        :return: The time of this FilteringOptimizerRuleResultList.  # noqa: E501
        :rtype: list[str]
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this FilteringOptimizerRuleResultList.


        :param time: The time of this FilteringOptimizerRuleResultList.  # noqa: E501
        :type: list[str]
        """

        self._time = time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FilteringOptimizerRuleResultList, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FilteringOptimizerRuleResultList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
